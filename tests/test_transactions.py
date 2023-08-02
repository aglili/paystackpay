import sys
import os 
import unittest
from dotenv import load_dotenv

load_dotenv()


TEST_KEY = os.getenv("TEST_KEY")


root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_folder)

from paystackpay.transaction import Transaction


class TestTransaction(unittest.TestCase):

    def setUp(self) -> None:
        self.transaction = Transaction(TEST_KEY)



    def test_initialize_transaction(self):
        email = "cecilselorm34@gmail.com"
        amount = 1000
        currency = "GHS"

        response = self.transaction.initialize_transaction(email=email,amount=amount,currency=currency)
        # print(response)
        self.assertEqual(response["status"],True)
        
    # def test_verify_transaction(self):
    #     reference_id  = "mko157u44s"
    #     response = self.transaction.verify_transaction(reference=reference_id)
    #     print(response)
    #     self.assertEqual(response["status"],True)


    # def test_transaction_list(self):
    #     response = self.transaction.transaction_list()
    #     self.assertEqual(response["status"], True)

    # def test_fetch_transaction(self):
    #     transaction_id = "some_transaction_id"
    #     response = self.transaction.fetch_transaction(transaction_id=transaction_id)
    #     self.assertEqual(response["status"], True)

    # def test_charge_authorization(self):
    #     email = "cecilselorm34@gmail.com"
    #     amount = 500
    #     auth_code = "some_authorization_code"
    #     response = self.transaction.charge_authorization(email=email, amount=amount, auth_code=auth_code)
    #     self.assertEqual(response["status"], True)

    # def test_view_transaction_timeline(self):
    #     tran_id_reference = "some_transaction_reference"
    #     response = self.transaction.view_transaction_timeline(tran_id_reference=tran_id_reference)
    #     self.assertEqual(response["status"], True)

    # def test_transaction_totals(self):
    #     response = self.transaction.transaction_totals()
    #     self.assertEqual(response["status"], True)

    # def test_export_transaction(self):
    #     response = self.transaction.export_transaction()
    #     self.assertEqual(response["status"], True)

    # def test_partial_debit(self):
    #     email = "cecilselorm34@gmail.com"
    #     amount = 200
    #     auth_code = "some_authorization_code"
    #     response = self.transaction.partial_debit(auth_code=auth_code, email=email, amount=amount)
    #     self.assertEqual(response["status"], True)



