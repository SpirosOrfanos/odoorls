recs = env['x_checks'].search([('x_name', '=', record.x_name)])
if (recs and len(recs)>1):
    raise UserError("existing name")


if (record.x_studio_ending_date):
    x_studio_ending_date_vld = record.x_studio_ending_date < datetime.date.today()
    if (x_studio_ending_date_vld) : 
        raise UserError("Ending Date must be after current date")


if (record.x_studio_issue_date):
    x_studio_issue_date_vld = record.x_studio_issue_date > datetime.date.today()
    if (x_studio_issue_date_vld) : 
        raise UserError("Issue Date must be before current date")