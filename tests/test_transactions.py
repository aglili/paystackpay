import sys
import os 
import unittest
from dotenv import load_dotenv
from unittest.mock import patch

load_dotenv()


TEST_KEY = os.getenv("TEST_KEY")


root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_folder)

from paystackpay.transaction import Transaction


class TestTransaction(unittest.TestCase):

    def setUp(self) -> None:
        self.transaction = Transaction(TEST_KEY)

    @patch("paystackpay.base.requests.post")
    def test_initialize_transaction(self, mock_post):
        from .mock_responses.mock_transactions import mock_initialize_transactions

        mock_post.return_value.json.return_value = mock_initialize_transactions
        mock_post.return_value.status = 200

        email = "cecilselorm34@gmail.com"
        amount = 1000
        currency = "GHS"

        response = self.transaction.initialize_transaction(email=email,amount=amount,currency=currency)
        self.assertEqual(response["status"],True)

    @patch("paystackpay.base.requests.get")
    def test_verify_transaction(self, mock_get):
        from .mock_responses.mock_transactions import mock_verify_transaction
        
        mock_get.return_value.json.return_value = mock_verify_transaction
        mock_get.return_value.status = 200

        reference_id  = "mko157u44s"
        response = self.transaction.verify_transaction(reference=reference_id)
        self.assertEqual(response["status"],True)
        self.assertEqual(response["data"]["reference"], reference_id)

    @patch("paystackpay.base.requests.get")
    def test_transaction_list(self, mock_get):
        from .mock_responses.mock_transactions import mock_list_transactions

        mock_get.return_value.json.return_value = mock_list_transactions
        mock_get.return_value.status = 200

        response = self.transaction.transaction_list()
        self.assertEqual(response["status"], True)
        self.assertEqual(response["data"][0]["status"], "success")

    @patch("paystackpay.base.requests.get")
    def test_fetch_transaction(self, mock_get):
        from .mock_responses.mock_transactions import mock_fetch_transactions

        mock_get.return_value.json.return_value = mock_fetch_transactions
        mock_get.return_value.status = 200

        transaction_id = "4099260516"
        response = self.transaction.fetch_transaction(transaction_id=transaction_id)
        self.assertEqual(response["status"], True)
        self.assertEqual(response["data"]["status"], "success")
        self.assertEqual(response["data"]["id"], int(transaction_id))

    @patch("paystackpay.base.requests.post")
    def test_charge_authorization(self, mock_post):
        from .mock_responses.mock_transactions import mock_charge_authorization

        mock_post.return_value.json.return_value = mock_charge_authorization
        mock_post.return_value.status = 200

        email = "cecilselorm34@gmail.com"
        amount = 500
        auth_code = "AUTH_uh8bcl3zbn"
        response = self.transaction.charge_authorization(email=email, amount=amount, auth_code=auth_code)
        self.assertEqual(response["status"], True)
        self.assertEqual(response["data"]["authorization"]["authorization_code"], auth_code)

    @patch("paystackpay.base.requests.get")
    def test_view_transaction_timeline(self, mock_get):
        from .mock_responses.mock_transactions import mock_transaction_timeline

        mock_get.return_value.json.return_value = mock_transaction_timeline
        mock_get.return_value.status = 200

        tran_id_reference = "some_transaction_reference"
        response = self.transaction.view_transaction_timeline(tran_id_reference=tran_id_reference)
        self.assertEqual(response["status"], True)
        self.assertEqual(response["data"]["success"], True)

    @patch("paystackpay.base.requests.get")
    def test_transaction_totals(self, mock_get):
        from .mock_responses.mock_transactions import mock_transaction_totals

        mock_get.return_value.json.return_value = mock_transaction_totals
        mock_get.return_value.status = 200

        response = self.transaction.transaction_totals()
        self.assertEqual(response["status"], True)
        self.assertEqual(response["message"], "Transaction totals")

    @patch("paystackpay.base.requests.get")                              
    def test_export_transaction(self, mock_get):
        from .mock_responses.mock_transactions import mock_export_transactions

        mock_get.return_value.json.return_value = mock_export_transactions
        mock_get.return_value.status = 200

        response = self.transaction.export_transaction()
        self.assertEqual(response["status"], True)
        self.assertEqual(response["message"], "Export successful")

    @patch("paystackpay.base.requests.post")
    def test_partial_debit(self, mock_post):
        from .mock_responses.mock_transactions import mock_partial_debit

        mock_post.return_value.json.return_value = mock_partial_debit
        mock_post.return_value.status = 200

        email = "cecilselorm34@gmail.com"
        amount = 200
        auth_code = "AUTH_uh8bcl3zbn"
        response = self.transaction.partial_debit(auth_code=auth_code, email=email, amount=amount)
        self.assertEqual(response["status"], True)
        self.assertEqual(response["data"]["authorization"]["authorization_code"], auth_code)