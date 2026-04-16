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

class TestTransferRecipients:
    def test_create(self, client):
        with respx.mock:
            respx.post(f"{BASE}/transferrecipient").mock(return_value=httpx.Response(200, json={"status": True, "data": {"recipient_code": "RCP_abc"}}))
            result = client.transfer_recipients.create(type="nuban", name="John Doe", account_number="0123456789", bank_code="058", currency="NGN")
            assert result["status"] is True
            assert result["data"]["recipient_code"] == "RCP_abc"

    def test_list(self, client):
        with respx.mock:
            respx.get(f"{BASE}/transferrecipient").mock(return_value=httpx.Response(200, json={"status": True, "data": []}))
            result = client.transfer_recipients.list()
            assert result["status"] is True

    def test_fetch(self, client):
        with respx.mock:
            respx.get(f"{BASE}/transferrecipient/RCP_abc").mock(return_value=httpx.Response(200, json={"status": True, "data": {"recipient_code": "RCP_abc"}}))
            result = client.transfer_recipients.fetch("RCP_abc")
            assert result["data"]["recipient_code"] == "RCP_abc"

    def test_update(self, client):
        with respx.mock:
            respx.put(f"{BASE}/transferrecipient/RCP_abc").mock(return_value=httpx.Response(200, json={"status": True, "data": {}}))
            result = client.transfer_recipients.update("RCP_abc", name="Jane Doe")
            assert result["status"] is True

    def test_delete(self, client):
        with respx.mock:
            respx.delete(f"{BASE}/transferrecipient/RCP_abc").mock(return_value=httpx.Response(200, json={"status": True, "message": "Recipient deleted"}))
            result = client.transfer_recipients.delete("RCP_abc")
            assert result["status"] is True

class TestAsyncTransferRecipients:
    async def test_create(self, async_client):
        with respx.mock:
            respx.post(f"{BASE}/transferrecipient").mock(return_value=httpx.Response(200, json={"status": True, "data": {"recipient_code": "RCP_abc"}}))
            result = await async_client.transfer_recipients.create(type="nuban", name="John Doe", account_number="0123456789", bank_code="058", currency="NGN")
            assert result["status"] is True
        await async_client._client.close()
