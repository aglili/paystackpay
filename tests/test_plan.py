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

        self.plan = Plan(TEST_KEY)


    def test_create_plan(self):

        plan_name = "Monthly Platinum Session"
        interval = "monthly"
        amount = 10000
        currency = "NGN"

        response = self.plan.create_plan(plan_name, interval, amount,currency)
        self.assertEqual(response["status"], True)

    def test_list_plans(self):
        response = self.plan.list_plans()
        self.assertEqual(response["status"], True)

    def test_fetch_plan(self):
        plan_id_or_code = "PLN_cfd3s2sdmqxravk"
        response = self.plan.fetch_plan(plan_id_or_code)
        self.assertEqual(response["status"], True)

    def test_update_plan(self):
        plan_id_or_code = "PLN_cfd3s2sdmqxravk"
        updated_plan_name = "Updated Plan"
        updated_interval = "weekly"
        updated_amount = 2000.0
        response = self.plan.update_plan(plan_name=updated_plan_name, interval=updated_interval, amount=updated_amount, id_or_code=plan_id_or_code)
        self.assertEqual(response["status"], True)



