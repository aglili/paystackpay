import httpx
import pytest
import respx

from paystackpay import AsyncPaystack, Paystack

BASE = "https://api.paystack.co"


@pytest.fixture
def client():
    return Paystack(secret_key="sk_test_123")


@pytest.fixture
def async_client():
    return AsyncPaystack(secret_key="sk_test_123")


class TestPaymentRequests:
    def test_create(self, client):
        with respx.mock:
            respx.post(f"{BASE}/paymentrequest").mock(
                return_value=httpx.Response(
                    200, json={"status": True, "data": {"request_code": "PRQ_abc"}}
                )
            )
            result = client.payment_requests.create(
                customer="CUS_abc", description="Invoice", amount=200.0, currency="NGN"
            )
            assert result["status"] is True

    def test_fetch(self, client):
        with respx.mock:
            respx.get(f"{BASE}/paymentrequest/PRQ_abc").mock(
                return_value=httpx.Response(200, json={"status": True, "data": {}})
            )
            result = client.payment_requests.fetch("PRQ_abc")
            assert result["status"] is True

    def test_list(self, client):
        with respx.mock:
            respx.get(f"{BASE}/paymentrequest").mock(
                return_value=httpx.Response(200, json={"status": True, "data": []})
            )
            result = client.payment_requests.list()
            assert result["status"] is True

    def test_verify(self, client):
        with respx.mock:
            respx.get(f"{BASE}/paymentrequest/verify/PRQ_abc").mock(
                return_value=httpx.Response(200, json={"status": True, "data": {}})
            )
            result = client.payment_requests.verify("PRQ_abc")
            assert result["status"] is True

    def test_send_notification_uses_post(self, client):
        with respx.mock:
            route = respx.post(f"{BASE}/paymentrequest/notify/PRQ_abc").mock(
                return_value=httpx.Response(200, json={"status": True, "data": {}})
            )
            result = client.payment_requests.send_notification("PRQ_abc")
            assert result["status"] is True
            assert route.called


class TestAsyncPaymentRequests:
    async def test_create(self, async_client):
        with respx.mock:
            respx.post(f"{BASE}/paymentrequest").mock(
                return_value=httpx.Response(200, json={"status": True, "data": {}})
            )
            result = await async_client.payment_requests.create(
                customer="CUS_abc", description="Invoice", amount=200.0, currency="NGN"
            )
            assert result["status"] is True
        await async_client._client.close()
