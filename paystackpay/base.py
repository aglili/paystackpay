import requests
from .errors import MissingAPIKeyErr,WrongMethodErr



class Base(object):
    BASE_URL = 'https://api.paystack.co'


    def __init__(self,secret_key) -> None:
        if not secret_key:
            raise MissingAPIKeyErr("Your API_KEY is missing")
        self.secret_key = secret_key

        


    def headers(self,data=None):
        header = {
            "Authorization": f"Bearer {self.secret_key}"
        }
        if data:
            header['Content-Type'] = "application/json"
        return header

    def make_request(self, method, endpoint, data=None,params=None):
        methods = {
            "GET":requests.get,
            "POST":requests.post,
            "DELETE":requests.delete,
            "PUT":requests.put
        }
        request_method = methods.get(method)

        if not request_method:
            raise WrongMethodErr("HTTP method is wrong")
        
        url = f"{self.BASE_URL}/{endpoint}"
        try:
            response = request_method(url,headers=self.headers(data=data),json=data)
            response.raise_for_status()
            response_json = response.json()
            return response_json
        except requests.exceptions.RequestException as e:
            raise Exception(f"error: {str(e)}")