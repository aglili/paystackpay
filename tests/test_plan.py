import sys
import os
import unittest
from dotenv import load_dotenv
from unittest.mock import patch

load_dotenv()


TEST_KEY = os.getenv("TEST_KEY")


root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_folder)

from paystackpay.plans import Plan


class TestPlan(unittest.TestCase):
    def setUp(self):
        self.plan = Plan(TEST_KEY)

    @patch("paystackpay.base.requests.post")
    def test_create_plan(self, mock_post):
        from .mock_responses.mock_plans import mock_create_plans

        mock_post.return_value.json.return_value = mock_create_plans
        mock_post.return_value.status = 200

        plan_name = "Monthly Platinum Session"
        interval = "monthly"
        amount = 10000
        currency = "NGN"

        response = self.plan.create_plan(plan_name, interval, amount,currency)
        self.assertEqual(response["status"], True)
        self.assertEqual(response["data"]["name"], plan_name)
        self.assertEqual(response["data"]["amount"], amount)

    @patch("paystackpay.base.requests.get")
    def test_list_plans(self, mock_get):
        from .mock_responses.mock_plans import mock_list_plans

        mock_get.return_value.json.return_value = mock_list_plans
        mock_get.return_value.status = 200

        response = self.plan.list_plans()
        self.assertEqual(response["status"], True)
        self.assertEqual(response["message"], "Plans retrieved")

    @patch("paystackpay.base.requests.get")
    def test_fetch_plan(self, mock_get):
        from .mock_responses.mock_plans import mock_fetch_plan

        mock_get.return_value.json.return_value = mock_fetch_plan
        mock_get.return_value.status = 200

        plan_id_or_code = "PLN_cfd3s2sdmqxravk"
        response = self.plan.fetch_plan(plan_id_or_code)
        self.assertEqual(response["status"], True)
        if str(plan_id_or_code):
            self.assertEqual(response["data"]["plan_code"], plan_id_or_code)
        else:
            self.assertEqual(response["data"]["id"], plan_id_or_code)


    @patch("paystackpay.base.requests.put")
    def test_update_plan(self, mock_put):
        from .mock_responses.mock_plans import mock_update_plan

        mock_put.return_value.json.return_value = mock_update_plan
        mock_put.return_value.status = 200
        
        plan_id_or_code = "PLN_cfd3s2sdmqxravk"
        updated_plan_name = "Updated Plan"
        updated_interval = "weekly"
        updated_amount = 2000.0
        response = self.plan.update_plan(plan_name=updated_plan_name, interval=updated_interval, amount=updated_amount, id_or_code=plan_id_or_code)
        self.assertEqual(response["status"], True)