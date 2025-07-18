x_studio_gl_creation = record.x_studio_reason_code.x_studio_gl_creation
letters_of_guarantees = record.x_studio_letters_of_guarantees
x_studio_transaction_value = record.x_studio_opap_transaction_value
  
if letters_of_guarantees:
    if x_studio_gl_creation: 
        if x_studio_gl_creation == True and (x_studio_transaction_value==0.0 or x_studio_transaction_value==0.0 or x_studio_transaction_value==0):
            raise UserError("transaction value must have value")

if letters_of_guarantees:
    if x_studio_gl_creation: 
        if x_studio_gl_creation == True and (record.price_unit>0.0 or record.price_unit>0.0 or record.price_unit>0):
            raise UserError("price_unit value have value 0")
