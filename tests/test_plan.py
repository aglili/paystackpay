import sys
import os 
import unittest
from dotenv import load_dotenv

load_dotenv()


TEST_KEY = os.getenv("TEST_KEY")


root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_folder)

from paystackpay.plans import Plan


class TestPlan(unittest.TestCase):
    def setUp(self):

        self.plan = Plan("YOUR_SECRET_KEY")


    def test_create_plan(self):

        plan_name = "Monthly Premium Session"
        interval = "monthly"
        amount = 1000.0
        currency = "GHS"

        response = self.plan.create_plan(plan_name, interval, amount,currency)
        self.assertEqual(response["status"], True)


