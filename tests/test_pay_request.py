import sys
import os 
import unittest
from unittest.mock import patch
from dotenv import load_dotenv

load_dotenv()


TEST_KEY = os.getenv("TEST_KEY")


root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_folder)

from paystackpay.pay_requests import PaymentRequest

class TestPaymentRequest(unittest.TestCase):

    def setUp(self) -> None:
        
        self.request = PaymentRequest(TEST_KEY)

    @patch("paystackpay.base.requests.post")
    def test_create_payment_request(self, mock_post):
        from .mock_responses.mock_pay_request import mock_create_pay_request

        mock_post.return_value.json.return_value = mock_create_pay_request
        mock_post.return_value.status = 200

        customer_id = "CUS_ravy504uywyao9w"
        description = "Payment For Hacks"
        currency = "GHS"
        amount = 1

        response = self.request.create_payment_request(customer_id=customer_id,description=description,amount=amount,currency=currency)
        #incomplete
        self.assertEqual(response['status'],True)

    @patch("paystackpay.base.requests.get")
    def test_fetch_payment_request(self, mock_get):
        from .mock_responses.mock_pay_request import mock_fetch_pay_request

        mock_get.return_value.json.return_value = mock_fetch_pay_request
        mock_get.return_value.status = 200

        request_code = "PRQ_53s49t73kq6qmsq"
        response = self.request.fetch_payment_request(request_code=request_code)
        self.assertEqual(response['status'],True)
        self.assertEqual(response['data']['request_code'], request_code)

    @patch("paystackpay.base.requests.get")
    def test_list_payment_requests(self, mock_get):
        from .mock_responses.mock_pay_request import mock_list_pay_request

        mock_get.return_value.json.return_value = mock_list_pay_request
        mock_get.return_value.status = 200

        response = self.request.list_payment_requests()
        self.assertEqual(response['status'],True)

    @patch("paystackpay.base.requests.get")
    def test_verify_payment_request(self, mock_get):
        from .mock_responses.mock_pay_request import mock_verify_pay_request

        mock_get.return_value.json.return_value = mock_verify_pay_request
        mock_get.return_value.status = 200

        request_code = "PRQ_53s49t73kq6qmsq"
        response = self.request.verify_payment_request(request_code=request_code)
        self.assertEqual(response['status'],True)
        self.assertEqual(response['data']['request_code'], request_code)

    @patch("paystackpay.base.requests.post")
    def test_send_notification(self, mock_post):
        from .mock_responses.mock_pay_request import mock_send_notification

        mock_post.return_value.json.return_value = mock_send_notification
        mock_post.return_value.status = 200

        request_code = "PRQ_53s49t73kq6qmsq"
        response = self.request.send_notification(request_code=request_code)
        self.assertEqual(response['status'], True)
        self.assertEqual(response['message'], "Notification sent")