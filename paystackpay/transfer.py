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
