from .base import Base
from pydantic import EmailStr
from .utils import validate_amount

class Transaction(Base):
    
    def initialize_transaction(self,email:EmailStr,amount:float,currency:str):
        endpoint = 'transaction/initialize'

        if currency == "GHS":
            validated_amount = validate_amount(amount)*100
        else:
            validated_amount = validate_amount(amount)

        

        data = {
            "email":email,
            "amount":str(validated_amount),
            "currency":currency
        }

        return self.make_request("POST",endpoint=endpoint,data=data)
    

    def verify_transaction(self,reference:str):
        endpoint = f"/transaction/verify/{reference}"

        return self.make_request("GET",endpoint=endpoint)
    

    def transaction_list(self):
        endpoint = 'transaction/'
        return self.make_request("GET",endpoint=endpoint)
    

    def fetch_transaction(self,transaction_id:str):
        endpoint = f"/transaction/{transaction_id}"
        return self.make_request("GET",endpoint=endpoint)
    

    def charge_authorization(self,email:EmailStr,amount:float,auth_code:str):
        endpoint = '/transaction/charge_authorization'

        validated_amount = validate_amount(amount=amount)*100

        data = {
            "email":email,
            "amount":str(validated_amount),
            "authorization_code":auth_code
        }

        return self.make_request("POST",endpoint=endpoint,data=data)

    def view_transaction_timeline(self,tran_id_reference:str):
        endpoint = f"/transaction/timeline/{tran_id_reference}"
        return self.make_request("GET",endpoint=endpoint)
    
    def transaction_totals(self):
        endpoint = '/transaction/totals'
        return self.make_request("GET",endpoint=endpoint)
    
    def export_transaction(self):
        endpoint = '/transaction/export'
        return self.make_request("GET",endpoint=endpoint)
    

    def partial_debit(self,auth_code:str,email:EmailStr,amount:float):
        endpoint = '/transaction/partial_debit'

        validated_amount = validate_amount(amount=amount)*100

        data = {
            "authorization_code":auth_code,
            "Currency":"GHS",
            "email":email,
            "amount" : str(validated_amount)
        }

        return self.make_request("POST",endpoint=endpoint,data=data)