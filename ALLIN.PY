for record in records:
    if record._name == 'account.move.line':
        move_type = record.move_id.move_type
        # INVOICES
        if (move_type == 'out_invoice'):
            invoice_date = record.invoice_date
            letters_of_guarantees = record.x_studio_letters_of_guarantees
            check_number = record.x_studio_check_number
            portfolio = record.x_studio_portfolio
            
            if (check_number and letters_of_guarantees):
                raise UserError("Both Check number and Letter of gurrantee seleted\nThis is not allowed")
            if (check_number and not portfolio):
                raise UserError("Check number must be used with a portfolo")
            if (portfolio and not check_number):
                raise UserError("portfolo must be used with a Check number")
#==============================================================================================
            #CHECKS actions
            if (check_number):
             
               
                if invoice_date and check_number and check_number.x_studio_issue_date and check_number.x_studio_issue_date >=invoice_date:
                    raise UserError(f"Check Issue date {check_number.x_studio_issue_date} must be before Invoice date {invoice_date}.")
                
                if invoice_date and check_number and check_number.x_studio_ending_date and check_number.x_studio_ending_date < invoice_date:
                   raise UserError(f"Ending Issue date {check_number.x_studio_ending_date} must be after or equal to Invoice date {invoice_date}.")
                
                if (record.x_studio_portfolio):
                  acc = portfolio.x_studio_account
                  record.x_studio_check_number.write({'x_studio_portfolio' : portfolio})
                  if acc:
                      record.write({'account_id': acc.id})  
                record.write({'price_unit': check_number.x_studio_check_amount})
               
#========================================================================================================                
            #LOG actions
            if (letters_of_guarantees):
                if invoice_date and letters_of_guarantees and letters_of_guarantees.x_studio_issue_date and letters_of_guarantees.x_studio_issue_date > invoice_date:
                    raise UserError(f"Invoice Date {invoice_date} muset be after Letter of Guarantee Issue date {letters_of_guarantees.x_studio_issue_date}.")
                
                if record.x_studio_letters_of_guarantees:
                    acc_ids = record.x_studio_letters_of_guarantees.x_studio_account
                    if acc_ids:
                        record.write({'account_id': acc_ids.id})
                
                if record.x_studio_letters_of_guarantees and record.x_studio_letters_of_guarantees.x_studio_amount:
                    record.write({'x_studio_opap_transaction_value': record.x_studio_letters_of_guarantees.x_studio_amount })
#------------------------------------------------------------------------------------------------------------------------------        
        # CREDIT-NOTE
        if (move_type == 'out_refund'):
            invoice_date = record.invoice_date
            letters_of_guarantees = record.x_studio_letters_of_guarantees
            check_number = record.x_studio_check_number
            portfolio = record.x_studio_portfolio
            
            if (check_number and not portfolio):
                raise UserError("Check number must be used with a portfolo")
            if (check_number and letters_of_guarantees):
                raise UserError("Both Check number and Letter of gurrantee seleted\nThis is not allowed")
            if (portfolio and not check_number):
                raise UserError("portfolo must be used with a Check number")
#==============================================================================================                
            #CHECKS actions
            if (check_number):
               
                     
                if invoice_date and check_number and check_number.x_studio_issue_date and check_number.x_studio_issue_date >=invoice_date:
                    raise UserError(f"Check Issue date {check_number.x_studio_issue_date} must be before Invoice date {invoice_date}.")

                if invoice_date and check_number and check_number.x_studio_ending_date and check_number.x_studio_ending_date < invoice_date:
                   raise UserError(f"Ending Issue date {check_number.x_studio_ending_date} must be after or equal to Invoice date {invoice_date}.")
                
                if (record.x_studio_portfolio):
                    acc = portfolio.x_studio_account
                    record.x_studio_check_number.write({'x_studio_portfolio' : portfolio})
                    if acc:
                        record.write({'account_id': acc.id})            
                if (record.price_unit):
                     record.x_studio_check_number.write({'x_studio_check_amount': record.price_unit})               
#==============================================================================================
            #LOG actions
            if (letters_of_guarantees):
                if invoice_date and letters_of_guarantees and letters_of_guarantees.x_studio_issue_date and letters_of_guarantees.x_studio_issue_date > invoice_date:
                    raise UserError(f"Invoice date {invoice_date} must be after {letters_of_guarantees.x_studio_issue_date}")
                
                if record.x_studio_letters_of_guarantees:
                    acc_ids = record.x_studio_letters_of_guarantees.x_studio_account
                    if acc_ids:
                        record.write({'account_id': acc_ids.id}) 
                
                if record.x_studio_letters_of_guarantees and record.x_studio_opap_transaction_value:
                    record.x_studio_letters_of_guarantees.write({'x_studio_amount' : record.x_studio_opap_transaction_value})
