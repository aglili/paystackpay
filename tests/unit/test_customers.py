import pytest
import httpx
import respx
from paystackpay import Paystack, AsyncPaystack

BASE = "https://api.paystack.co"

@pytest.fixture
def client():
    return Paystack(secret_key="sk_test_123")

@pytest.fixture
def async_client():
    return AsyncPaystack(secret_key="sk_test_123")

class TestCustomers:
    def test_create(self, client):
        with respx.mock:
            respx.post(f"{BASE}/customer").mock(return_value=httpx.Response(200, json={"status": True, "data": {"email": "test@example.com"}}))
            result = client.customers.create(email="test@example.com", first_name="John", last_name="Doe", phone="0201234567")
            assert result["status"] is True
            assert result["data"]["email"] == "test@example.com"

    def test_list(self, client):
        with respx.mock:
            respx.get(f"{BASE}/customer").mock(return_value=httpx.Response(200, json={"status": True, "data": []}))
            result = client.customers.list()
            assert result["status"] is True

    def test_fetch(self, client):
        with respx.mock:
            respx.get(f"{BASE}/customer/CUS_abc123").mock(return_value=httpx.Response(200, json={"status": True, "data": {"customer_code": "CUS_abc123"}}))
            result = client.customers.fetch("CUS_abc123")
            assert result["data"]["customer_code"] == "CUS_abc123"

    def test_update(self, client):
        with respx.mock:
            respx.put(f"{BASE}/customer/CUS_abc123").mock(return_value=httpx.Response(200, json={"status": True, "data": {}}))
            result = client.customers.update("CUS_abc123", first_name="Jane")
            assert result["status"] is True

    def test_update_only_sends_provided_fields(self, client):
        with respx.mock:
            import json
            route = respx.put(f"{BASE}/customer/CUS_abc123").mock(return_value=httpx.Response(200, json={"status": True, "data": {}}))
            client.customers.update("CUS_abc123", first_name="Jane")
            body = json.loads(route.calls[0].request.content)
            assert "first_name" in body
            assert "last_name" not in body

    def test_whitelist(self, client):
        with respx.mock:
            respx.post(f"{BASE}/customer/set_risk_action").mock(return_value=httpx.Response(200, json={"status": True, "data": {}}))
            result = client.customers.whitelist("CUS_abc123")
            assert result["status"] is True

    def test_blacklist(self, client):
        with respx.mock:
            respx.post(f"{BASE}/customer/set_risk_action").mock(return_value=httpx.Response(200, json={"status": True, "data": {}}))
            result = client.customers.blacklist("CUS_abc123")
            assert result["status"] is True

    def test_deactivate_authorization(self, client):
        with respx.mock:
            respx.post(f"{BASE}/customer/deactivate_authorization").mock(return_value=httpx.Response(200, json={"status": True, "data": {}}))
            result = client.customers.deactivate_authorization("AUTH_abc")
            assert result["status"] is True

class TestAsyncCustomers:
    async def test_create(self, async_client):
        with respx.mock:
            respx.post(f"{BASE}/customer").mock(return_value=httpx.Response(200, json={"status": True, "data": {"email": "test@example.com"}}))
            result = await async_client.customers.create(email="test@example.com", first_name="John", last_name="Doe", phone="0201234567")
            assert result["status"] is True
        await async_client._client.close()

    async def test_list(self, async_client):
        with respx.mock:
            respx.get(f"{BASE}/customer").mock(return_value=httpx.Response(200, json={"status": True, "data": []}))
            result = await async_client.customers.list()
            assert result["status"] is True
        await async_client._client.close()
