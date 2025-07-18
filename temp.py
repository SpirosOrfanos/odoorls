for record in records:
    if record._name == 'account.move.line':
        move_type = record.move_id.move_type
        # INVOICES
        if (move_type == 'out_invoice'):
            business_segment = record.x_studio_business_segment
            reason_code = record.x_studio_reason_code
            if (reason_code and business_segment):
                business_segment_value = record.x_studio_business_segment.id
                reason_code_value = record.x_studio_reason_code.id
                dtr = f"{reason_code_value},{business_segment_value}"
                dtr1 = f"{reason_code_value}"
                dtr2 = f"{business_segment_value}"
                vals = {
                    'analytic_distribution': {
                        dtr: 100
                    }
                }
                recordwrite({
                    'analytic_distribution': {
                        dtr: 100
                    }
                })
                #raise UserError(dtr)   
                
                #analytic_distribution = record.analytic_distribution
                #if (analytic_distribution):
                #    fic = dict(analytic_distribution)
                #    ldf = ""
                #    for fruit in fic.keys():
                #        ldf = ldf + "\n"+ (f"key {fruit} is {fic[fruit]}.")
                    #raise UserError(ldf)   
                #record.write(vals)
                #record.write({
                #    'analytic_distribution': {
                #        dtr: 100
                #    }
                #})
                #raise UserError(dtr)
            
           #------------------------------------------------------------------------------------------------------------------------------        
#        if (move_type == 'out_refund'):
#            business_segment = record.x_studio_business_segment
#            reason_code = record.x_studio_reason_code
#            if (reason_code and business_segment):
#                business_segment_value = record.x_studio_business_segment.id
#                reason_code_value = record.x_studio_reason_code.id
#                dtr = f"{business_segment_value},{reason_code_value}"
#                vals = {
#                    'analytic_distribution': {
#                        dtr: 100
#                    }
#                }
#                record.write(vals)
#                #record.write({
#                #    'analytic_distribution': {
#                #        dtr: 100
#                #    }
#                #})
#                #raise UserError(dtr)