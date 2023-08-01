import sys
import os 
import unittest
from dotenv import load_dotenv

load_dotenv()


TEST_KEY = os.getenv("TEST_KEY")


root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_folder)


from paystackpay.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self) -> None:
        self.customer = Customer(TEST_KEY)


    def test_create_customer(self):
        # Test create_customer method
        email = "test@example.com"
        first_name = "John"
        last_name = "Doe"
        phone = "1234567890"

        response = self.customer.create_customer(email=email,first_name=first_name,last_name=last_name,phone=phone)
        self.assertEqual(response["status"],True)
        self.assertEqual(response["data"]["email"],email)

    def test_list_customer(self):
        response = self.customer.list_costumers()
        self.assertEqual(response["status"], True)

    def test_fetch_customer(self):
        email_or_customer_code = "test@example.com"
        response = self.customer.fetch_customer(email_or_customer_code)
        self.assertEqual(response["status"], True)


    def test_update_customer(self):
        customer_code = "CUS_ng9mw56ma4cx6x9"
        first_name = "UpdatedFirstName"
        last_name = "UpdatedLastName"

        response = self.customer.update_customer(customer_code, first_name=first_name, last_name=last_name)
        self.assertEqual(response["status"], True)


    ## the endpoint for these two does not exist
    def test_whitelist_customer(self):
        customer_code = "CUS_ng9mw56ma4cx6x9"
        response = self.customer.whitelist_customer(customer_code)
        self.assertEqual(response["status"], True)
      

    def test_blacklist_customer(self):
        customer_code = "CUS_1234567890"
        response = self.customer.blacklist_customer(customer_code)
        self.assertEqual(response["status"], True)
       



    