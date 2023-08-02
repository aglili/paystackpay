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
        
    def test_verify_transaction(self):
        reference_id  = "mko157u44s"
        response = self.transaction.verify_transaction(reference=reference_id)
        print(response)
        self.assertEqual(response["status"],True)



