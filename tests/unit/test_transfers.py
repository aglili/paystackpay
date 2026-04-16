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

class TestTransfers:
    def test_initiate(self, client):
        with respx.mock:
            respx.post(f"{BASE}/transfer").mock(return_value=httpx.Response(200, json={"status": True, "data": {"transfer_code": "TRF_abc"}}))
            result = client.transfers.initiate(amount=100.0, recipient="RCP_abc", reason="Test", currency="NGN")
            assert result["status"] is True

    def test_initiate_converts_amount(self, client):
        with respx.mock:
            route = respx.post(f"{BASE}/transfer").mock(return_value=httpx.Response(200, json={"status": True, "data": {}}))
            client.transfers.initiate(amount=100.0, recipient="RCP_abc", reason="Test", currency="NGN")
            body = json.loads(route.calls[0].request.content)
            assert body["amount"] == 10000

    def test_finalize(self, client):
        with respx.mock:
            respx.post(f"{BASE}/transfer/finalize_transfer").mock(return_value=httpx.Response(200, json={"status": True, "data": {}}))
            result = client.transfers.finalize(transfer_code="TRF_abc", otp="123456")
            assert result["status"] is True

    def test_fetch(self, client):
        with respx.mock:
            respx.get(f"{BASE}/transfer/TRF_abc").mock(return_value=httpx.Response(200, json={"status": True, "data": {"transfer_code": "TRF_abc"}}))
            result = client.transfers.fetch("TRF_abc")
            assert result["data"]["transfer_code"] == "TRF_abc"

    def test_list(self, client):
        with respx.mock:
            respx.get(f"{BASE}/transfer").mock(return_value=httpx.Response(200, json={"status": True, "data": []}))
            result = client.transfers.list()
            assert result["status"] is True

class TestAsyncTransfers:
    async def test_initiate(self, async_client):
        with respx.mock:
            respx.post(f"{BASE}/transfer").mock(return_value=httpx.Response(200, json={"status": True, "data": {}}))
            result = await async_client.transfers.initiate(amount=100.0, recipient="RCP_abc", reason="Test", currency="NGN")
            assert result["status"] is True
        await async_client._client.close()
