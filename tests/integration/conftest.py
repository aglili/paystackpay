import os
import pytest


@pytest.fixture
def client():
    from paystackpay import Paystack
    return Paystack(secret_key=os.environ["PAYSTACK_TEST_KEY"])


@pytest.fixture
def async_client():
    from paystackpay import AsyncPaystack
    return AsyncPaystack(secret_key=os.environ["PAYSTACK_TEST_KEY"])
