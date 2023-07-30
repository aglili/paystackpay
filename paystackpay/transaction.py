from .base import Base
from pydantic import EmailStr
from .utils import validate_amount

class Transaction(Base):
    
    def initialize_transaction(self,email:EmailStr,amount):
        endpoint = 'transaction/initialize'
        validate_amount = validate_amount(amount)

        data = {
            "email":email,
            "amount":validate_amount
        }

        return self.make_request("POST",endpoint=endpoint,data=data)
    

    def verify_transaction(self,reference):
        endpoint = f"/transaction/verify/{reference}"

        return self.make_request("POST",endpoint=endpoint)
    

    def transaction_list(self):
        endpoint = 'transaction/'
        return self.make_request("GET",endpoint=endpoint)
