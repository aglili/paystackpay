import pytest
import httpx
import respx
import json as json_mod
from paystackpay import Paystack, AsyncPaystack

BASE = "https://api.paystack.co"

@pytest.fixture
def client():
    return Paystack(secret_key="sk_test_123")

@pytest.fixture
def async_client():
    return AsyncPaystack(secret_key="sk_test_123")

class TestRefunds:
    def test_create(self, client):
        with respx.mock:
            respx.post(f"{BASE}/refund").mock(return_value=httpx.Response(200, json={"status": True, "data": {"id": 1}}))
            result = client.refunds.create(transaction="ref123")
            assert result["status"] is True

    def test_create_with_amount(self, client):
        with respx.mock:
            route = respx.post(f"{BASE}/refund").mock(return_value=httpx.Response(200, json={"status": True, "data": {}}))
            client.refunds.create(transaction="ref123", amount=50.0, currency="NGN")
            body = json_mod.loads(route.calls[0].request.content)
            assert body["amount"] == 5000

    def test_list(self, client):
        with respx.mock:
            respx.get(f"{BASE}/refund").mock(return_value=httpx.Response(200, json={"status": True, "data": []}))
            result = client.refunds.list()
            assert result["status"] is True

    def test_fetch(self, client):
        with respx.mock:
            respx.get(f"{BASE}/refund/1").mock(return_value=httpx.Response(200, json={"status": True, "data": {"id": 1}}))
            result = client.refunds.fetch(1)
            assert result["data"]["id"] == 1

class TestAsyncRefunds:
    async def test_create(self, async_client):
        with respx.mock:
            respx.post(f"{BASE}/refund").mock(return_value=httpx.Response(200, json={"status": True, "data": {}}))
            result = await async_client.refunds.create(transaction="ref123")
            assert result["status"] is True
        await async_client._client.close()
