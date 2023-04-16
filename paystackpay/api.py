import requests


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
        response = requests.get(endpoint,headers=self.headers(),params=params)
        return response.json()
    


