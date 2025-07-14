for record in records:
    if record._name == 'account.move.line':
        move_type = record.move_id.move_type
        if (move_type == 'entry'):
            invoice_date = record.date
            check_number = record.x_studio_check_number
            portfolio = record.x_studio_portfolio
            
            
            if (check_number and not portfolio):
                raise UserError("Check number must be used with a portfolo")
            if (portfolio and not check_number):
                raise UserError("portfolo must be used with a Check number")

            #CHECKS actions
            if (check_number):
             
                if invoice_date and check_number and check_number.x_studio_issue_date and check_number.x_studio_issue_date >invoice_date:
                    raise UserError(f"Check Issue date {check_number.x_studio_issue_date} must be before Invoice date {invoice_date}.")
                if invoice_date and check_number and check_number.x_studio_ending_date and check_number.x_studio_ending_date < invoice_date:
                   raise UserError(f"Ending Issue date {check_number.x_studio_ending_date} must be after or equal to Invoice date {invoice_date}.")
                if (record.x_studio_portfolio):
                  acc = portfolio.x_studio_account
                  #record.x_studio_check_number.write({'x_studio_portfolio' : portfolio})
                  if acc:
                      record.write({'account_id': acc.id})  
                record.write({'credit': check_number.x_studio_check_amount})
               