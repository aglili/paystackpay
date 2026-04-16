import pytest
import httpx
import respx
import json
from paystackpay import Paystack, AsyncPaystack

BASE = "https://api.paystack.co"

@pytest.fixture
def client():
    return Paystack(secret_key="sk_test_123")

@pytest.fixture
def async_client():
    return AsyncPaystack(secret_key="sk_test_123")

class TestPlans:
    def test_create(self, client):
        with respx.mock:
            respx.post(f"{BASE}/plan").mock(return_value=httpx.Response(200, json={"status": True, "data": {"plan_code": "PLN_abc"}}))
            result = client.plans.create(name="Monthly", interval="monthly", amount=50.0, currency="GHS")
            assert result["status"] is True

    def test_create_converts_amount_to_subunit(self, client):
        with respx.mock:
            route = respx.post(f"{BASE}/plan").mock(return_value=httpx.Response(200, json={"status": True, "data": {}}))
            client.plans.create(name="Monthly", interval="monthly", amount=50.0, currency="GHS")
            body = json.loads(route.calls[0].request.content)
            assert body["amount"] == 5000

    def test_list(self, client):
        with respx.mock:
            respx.get(f"{BASE}/plan").mock(return_value=httpx.Response(200, json={"status": True, "data": []}))
            result = client.plans.list()
            assert result["status"] is True

    def test_fetch(self, client):
        with respx.mock:
            respx.get(f"{BASE}/plan/PLN_abc").mock(return_value=httpx.Response(200, json={"status": True, "data": {"plan_code": "PLN_abc"}}))
            result = client.plans.fetch("PLN_abc")
            assert result["data"]["plan_code"] == "PLN_abc"

    def test_update(self, client):
        with respx.mock:
            respx.put(f"{BASE}/plan/PLN_abc").mock(return_value=httpx.Response(200, json={"status": True, "data": {}}))
            result = client.plans.update("PLN_abc", name="Annual")
            assert result["status"] is True

    def test_update_only_sends_provided_fields(self, client):
        with respx.mock:
            route = respx.put(f"{BASE}/plan/PLN_abc").mock(return_value=httpx.Response(200, json={"status": True, "data": {}}))
            client.plans.update("PLN_abc", name="Annual")
            body = json.loads(route.calls[0].request.content)
            assert "name" in body
            assert "interval" not in body

class TestAsyncPlans:
    async def test_create(self, async_client):
        with respx.mock:
            respx.post(f"{BASE}/plan").mock(return_value=httpx.Response(200, json={"status": True, "data": {}}))
            result = await async_client.plans.create(name="Monthly", interval="monthly", amount=50.0, currency="NGN")
            assert result["status"] is True
        await async_client._client.close()
