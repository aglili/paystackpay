import sys
import os 
import unittest
from dotenv import load_dotenv

load_dotenv()


TEST_KEY = os.getenv("TEST_KEY")


root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_folder)

from paystackpay.pay_requests import PaymentRequest

class TestPaymentRequest(unittest.TestCase):

    def setUp(self) -> None:
        
        self.request = PaymentRequest(TEST_KEY)

    # def test_create_payment_request(self):
    #     customer_id = "CUS_ravy504uywyao9w"
    #     description = "Payment For Hacks"
    #     currency = "GHS"
    #     amount = 1

    #     response = self.request.create_payment_request(customer_id=customer_id,description=description,amount=amount,currency=currency)
    #     print(response)
    #     self.assertEqual(response['status'],True)


    # def test_fetch_payment_request(self):
    #     request_code = "PRQ_53s49t73kq6qmsq"
    #     response = self.request.fetch_payment_request(request_code=request_code)
    #     self.assertEqual(response['status'],True)

    # def test_list_payment_requests(self):
    #     response = self.request.list_payment_requests()
    #     print(response)


    
    # def test_verify_payment_request(self):
    #     request_code = "PRQ_53s49t73kq6qmsq"
    #     response = self.request.verify_payment_request(request_code=request_code)
    #     print(response)
    #     self.assertEqual(response['status'],True)

    def test_send_notification(self):
        request_code = "PRQ_53s49t73kq6qmsq"
        response = self.request.send_notification(request_code=request_code)
        print(response)
        self.assertEqual(response['status'],True)




