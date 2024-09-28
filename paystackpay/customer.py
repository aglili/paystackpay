from .base import Base
from pydantic import EmailStr

class Customer(Base):

    def create_customer(self,email:EmailStr,first_name:str,last_name:str,phone:str):
        endpoint = 'customer'
        data = {
            "email":email,
            "first_name":first_name,
            "last_name":last_name,
            "phone": phone
        }
        return self.make_request("POST",endpoint=endpoint,data=data)

    def list_costumers(self):
        endpoint = 'customer'
        return self.make_request("GET",endpoint=endpoint)    

    def fetch_customer(self,email_or_customer_code:str):
        endpoint = f"customer/{email_or_customer_code}"
        return self.make_request("GET",endpoint=endpoint)
    
    def update_customer(self,customer_code:str,first_name:str=None,last_name:str=None,email:EmailStr=None,phone=None):
        endpoint = f"customer/{customer_code}"

        data = {}

        if first_name is not None:
            data["first_name"] = first_name
        if last_name is not None:
            data["last_name"] = last_name
        if email is not None:
            data["email"] = email
        if phone is not None:
            data["phone"] = phone

        return self.make_request("PUT",endpoint=endpoint,data=data)
    

    def whitelist_customer(self,customer_code:str):
        endpoint = f"customer/set_risk_action"

        data = {
            "customer":customer_code,
            "risk_action":"allow"
        }

        return self.make_request("POST",endpoint=endpoint,data=data)
    

    def blacklist_customer(self,customer_code:str):
        endpoint = f"customer/set_risk_action"

        data = {
            "customer":customer_code,
            "risk_action":"deny"
        }

        return self.make_request("POST",endpoint=endpoint,data=data)
    
    def deactivate_auth(self,auth_code:str):
        endpoint = "customer/deactivate_authorization"

        data = {
            "authorization_code":auth_code
        }

        return self.make_request("POST",endpoint=endpoint,data=data)



    



    
    
    