from errors import InvalidDataErr

def validate_amount(amount):
    if not amount:
        raise InvalidDataErr("Amount Is Required")
    
    if isinstance(amount,int) or isinstance(amount,float):
        if amount < 0:
            raise InvalidDataErr("Amount Should Be Greater than Zero")
        return amount
    else:
        raise InvalidDataErr("Amount Should be a number")
        


    
