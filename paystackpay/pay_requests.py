from .base import Base



class PaymentRequest(Base):

    def create_payment_request(self,customer_id:str,description:str,amount:float,currency:str):
        endpoint = "paymentrequest"

        if currency == "GHS":
            amount = amount*100

        data = {
            "description":description,
            "amount":int(amount),
            "customer": customer_id,
            "currency" : currency
        }

        return self.make_request("POST",endpoint=endpoint,data=data)
    
    def fetch_payment_request(self,request_code:str):
        endpoint = f"paymentrequest/{request_code}"
        return self.make_request("GET",endpoint=endpoint)
    

    def list_payment_requests(self):
        endpoint = 'paymentrequest'
        return self.make_request("GET",endpoint=endpoint)


    def verify_payment_request(self,request_code:str):
        endpoint = f"paymentrequest/verify/{request_code}"
        return self.make_request("GET",endpoint=endpoint)
    
    def send_notification(self,request_code:str):
        endpoint = f"paymentrequest/notify/{request_code}"
        return self.make_request("POST",endpoint=endpoint)
    


