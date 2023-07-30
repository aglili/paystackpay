import requests
from pydantic import EmailStr
from .utils import validate_amount
from .errors import InvalidDataErr

class PayStackAPI():

    """API Wrapper for Paystack API written by https://github.com/aglili"""

    BASE_URL = 'https://api.paystack.co'

    def __init__(self,secret_key):
        self.secret_key = secret_key

    def headers(self):
        return {
             "Authorization": f"Bearer {self.secret_key}",
            "Content-Type": "application/json"
        }

    def verify_account_number(self,account_number:int,bank_code:int):
        endpoint = f"{self.BASE_URL}/bank/resolve"
        params = {
            "account_number":account_number,
            "bank_code":bank_code,
        }
        response = requests.get(endpoint,headers=self.headers(),params=params).json()
        return response
        
    def accept_payment(self, email:EmailStr, metadata, amount:float):
        endpoint = f"{self.BASE_URL}/transaction/initialize"
        data = {
            "email": email, #email of person making payment
            "amount": 100 * amount, #amount needs to be multiplied by 100 so if amount is GHS10, it will become 10*100 = 1000
            "metadata": metadata #json eg {'application':'PayStack', 'user':'John Doe'}
        }
        response = requests.post(endpoint, json=data, headers=self.headers()).json()
        return response

    def add_customer(self, name:str, number:str, email:EmailStr, currency:str):
        endpoint = f"{self.BASE_URL}/customer"
        data = {
            "email": email,
            "first_name": name,
            "phone": number,
            "currency": currency #eg: GHS
        }
        response = requests.post(endpoint, json=data, headers=self.headers()).json()
        return response
    
    def update_customer(self,code, first_name:str,last_name:str,phone:str):
        url = f'https://api.paystack.co/customer/{code}'
        data = {
            'first_name': first_name,
            'last_name': last_name,
            "phone":phone
        }
        response = requests.put(url, headers=self.headers(), json=data)
        response_json = response.json()
        return response_json
    
    
    def create_payment_request(self, description, line_items, tax, customer, due_date):
        url = 'https://api.paystack.co/paymentrequest'
        data = {
            'description': description,
            'line_items': line_items,
            'tax': tax,
            'customer': customer,
            'due_date': due_date
        }
        response = requests.post(url, headers=self.headers(), json=data)
        response_json = response.json()
        return response_json

    def show_customer_list(self):
        endpoint = f"{self.BASE_URL}/customer"
        response = requests.get(endpoint, headers=self.headers()).json()
        return response
        
    def pay_customer(self, amount:float, recipient:str, reason:str):
        if not amount:
            raise InvalidDataErr("Amount is Needed")
        
        validated_amount = validate_amount(amount=amount)
        
        if not recipient:
            raise InvalidDataErr("A Recipient is Needed")
        
        if not reason:
            raise InvalidDataErr("Reason for Transaction is Needed")

        endpoint = f"{self.BASE_URL}/transfer"
        data = {
            "source": "balance",
            "reason": reason,
            "amount":100 * validated_amount,
            "recipient": recipient
        }

        response = requests.post(endpoint, json=data, headers=self.headers()).json()
        return response