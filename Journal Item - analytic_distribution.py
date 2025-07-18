for record in records:
    if record._name == 'account.move.line':
        move_type = record.move_id.move_type
        # INVOICES
        if (move_type == 'out_invoice' or move_type == 'out_refund'):
           
            business_segment = record.x_studio_business_segment
            reason_code = record.x_studio_reason_code
            cid = record.company_id.id
            
            if (reason_code or business_segment):
                rcid = 'none'
                bsid = 'none'
                if (reason_code):
                    reason_code_value = record.x_studio_reason_code.x_studio_reason_code
                    reason_code_value_ref = env['account.analytic.account'].search([
                        ('name', '=', str(reason_code_value)),
                        ('plan_id', '=', 'Reason Code'),
                        ('company_id.id', '=', str(cid))
                    ], order='id desc', limit=1)
                    if (reason_code_value_ref):
                        rcid = str(reason_code_value_ref.id)
                
                if (business_segment):
                    business_segment_value = record.x_studio_business_segment.x_studio_business_segment_code_1
                    business_segment_value_ref = env['account.analytic.account'].search([
                        ('name', '=', business_segment_value),
                        ('plan_id', '=', 'Business Segment'),
                        ('company_id.id', '=', str(cid))
                    ], order='id desc', limit=1)
                
                    if (business_segment_value_ref):
                        bsid = str(business_segment_value_ref.id)
                
              
                if (rcid!="none" and bsid!="none"):
                    fname = rcid + "," + bsid
                    vals = { 'analytic_distribution': { fname : 100 } }
                    record.write(vals )
                elif (rcid!="none"):
                    vals = { 'analytic_distribution': { int(rcid) : 100 } }
                    record.write(vals )
                elif (bsid!="none"):
                    vals = { 'analytic_distribution': { int(bsid) : 100 } }
                    record.write(vals )
                elif (rcid=="none" and bsid=="none"):
                    vals = {
                        'analytic_distribution': {
                        
                        }
                    }
                    record.write(vals)
            else:
                vals = {
                    'analytic_distribution': {
                        
                    }
                }
                record.write(vals)