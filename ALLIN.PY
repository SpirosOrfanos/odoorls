for record in records:
    if record._name == 'account.move.line':
        move_type = record.move_id.move_type
        # INVOICES
        if (move_type == 'out_invoice'):
            invoice_date = record.invoice_date
            letters_of_guarantees = record.x_studio_letters_of_guarantees
            if invoice_date and letters_of_guarantees and letters_of_guarantees.x_studio_issue_date and letters_of_guarantees.x_studio_issue_date > invoice_date:
                raise UserError(f"Invoice Date {invoice_date} muset be after Letter of Guarantee Issue date {letters_of_guarantees.x_studio_issue_date}.")
            if record.x_studio_letters_of_guarantees:
               acc_ids = record.x_studio_letters_of_guarantees.x_studio_account
               if acc_ids:
                   record.write({'account_id': acc_ids.id})
            if record.x_studio_letters_of_guarantees and record.x_studio_letters_of_guarantees.x_studio_amount:
                record.write({'x_studio_opap_transaction_value': record.x_studio_letters_of_guarantees.x_studio_amount })
        # CREDIT-NOTE
        if (move_type == 'out_refund'):
            invoice_date = record.invoice_date
            letters_of_guarantees = record.x_studio_letters_of_guarantees
            if invoice_date and letters_of_guarantees and letters_of_guarantees.x_studio_issue_date and letters_of_guarantees.x_studio_issue_date > invoice_date:
                raise UserError(f"Invoice date {invoice_date} must be after {letters_of_guarantees.x_studio_issue_date}")
            if record.x_studio_letters_of_guarantees:
               record.x_studio_letters_of_guarantees.write({'x_studio_account': record.account_id})  
            if record.x_studio_letters_of_guarantees and record.x_studio_opap_transaction_value:
                record.x_studio_letters_of_guarantees.write({'x_studio_amount' : record.x_studio_opap_transaction_value})
