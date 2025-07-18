recs = env['res.partner'].search([('x_studio_code', '=', record.x_studio_code)])
if (recs and len(recs)>1):
    raise UserError("existing code")