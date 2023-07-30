from .base import Base

class Customer(Base):


    def verify_account_number(self,account_number: int, bank_code: int):
        endpoint = 'bank/resolve'
        params = {
            "account_number":account_number,
            "bank_code":bank_code
        }

        return self.make_request("GET",endpoint=endpoint,params=params)
    
    