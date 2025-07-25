if (record.x_studio_issue_date):
    x_studio_issue_date_validation = record.x_studio_issue_date > datetime.date.today()
    if (x_studio_issue_date_validation) : 
        raise UserError("Issue date can not be be after current date")
        
if (record.x_studio_expiration_date):
    x_studio_expiration_date_validation = record.x_studio_expiration_date <= datetime.date.today()
    if (x_studio_expiration_date_validation) : 
        raise UserError("expiration date can not be be before current dfate")


if (record.x_studio_expiration_date and record.x_studio_issue_date and record.x_studio_issue_date >= record.x_studio_expiration_date):
    raise UserError("expiration must be after Issue date")

recs = env['x_letters_of_guarantee'].search([('x_name', '=', record.x_name)])
if (recs and len(recs)>1):
    raise UserError("existing number")