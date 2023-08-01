from .base import Base
from .utils import validate_amount


class Transaction(Base):

    def initiate_transfer(self,amount:float,receipient:str,reason:str,currency:str):
        endpoint = '/transfer'

        if currency == "GHS":
            amount = amount*100

        validated_amount = validate_amount(amount)

        data = {
            "amount": validated_amount,
            "reason":reason,
            "source":"balance",
            "recipient":receipient
        }

        return self.make_request("POST",endpoint=endpoint,data=data)
    

    def finalize_transfer(self,transfer_code:str,otp:str):
        endpoint = '/transfer/finalize_transfer'
        data  = {
            "transfer_code":transfer_code,
            "otp":otp
        }
        return self.make_request("POST",endpoint=endpoint,data=data)
    
    def fetch_transfer(self,transfer_id:str):
        endpoint = f"/transfer/{transfer_id}"
        return self.make_request("GET",endpoint=endpoint)
    


