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


class TestTransactions:
    def test_initialize(self, client):
        with respx.mock:
            respx.post(f"{BASE}/transaction/initialize").mock(
                return_value=httpx.Response(200, json={"status": True, "data": {"authorization_url": "https://checkout.paystack.com/abc", "reference": "ref123"}})
            )
            result = client.transactions.initialize(email="test@example.com", amount=100.0, currency="GHS")
            assert result["status"] is True
            assert "authorization_url" in result["data"]

    def test_initialize_converts_amount_to_subunit(self, client):
        with respx.mock:
            route = respx.post(f"{BASE}/transaction/initialize").mock(
                return_value=httpx.Response(200, json={"status": True, "data": {}})
            )
            client.transactions.initialize(email="test@example.com", amount=100.0, currency="GHS")
            sent = route.calls[0].request
            import json
            body = json.loads(sent.content)
            assert body["amount"] == 10000

    def test_verify(self, client):
        with respx.mock:
            respx.get(f"{BASE}/transaction/verify/ref123").mock(
                return_value=httpx.Response(200, json={"status": True, "data": {"status": "success"}})
            )
            result = client.transactions.verify("ref123")
            assert result["status"] is True

    def test_list(self, client):
        with respx.mock:
            respx.get(f"{BASE}/transaction").mock(
                return_value=httpx.Response(200, json={"status": True, "data": []})
            )
            result = client.transactions.list()
            assert result["status"] is True

    def test_fetch(self, client):
        with respx.mock:
            respx.get(f"{BASE}/transaction/42").mock(
                return_value=httpx.Response(200, json={"status": True, "data": {"id": 42}})
            )
            result = client.transactions.fetch(42)
            assert result["data"]["id"] == 42

    def test_charge_authorization(self, client):
        with respx.mock:
            respx.post(f"{BASE}/transaction/charge_authorization").mock(
                return_value=httpx.Response(200, json={"status": True, "data": {}})
            )
            result = client.transactions.charge_authorization(
                email="test@example.com", amount=50.0, authorization_code="AUTH_abc", currency="NGN"
            )
            assert result["status"] is True

    def test_timeline(self, client):
        with respx.mock:
            respx.get(f"{BASE}/transaction/timeline/ref123").mock(
                return_value=httpx.Response(200, json={"status": True, "data": {}})
            )
            result = client.transactions.timeline("ref123")
            assert result["status"] is True

    def test_totals(self, client):
        with respx.mock:
            respx.get(f"{BASE}/transaction/totals").mock(
                return_value=httpx.Response(200, json={"status": True, "data": {}})
            )
            result = client.transactions.totals()
            assert result["status"] is True

    def test_export(self, client):
        with respx.mock:
            respx.get(f"{BASE}/transaction/export").mock(
                return_value=httpx.Response(200, json={"status": True, "data": {}})
            )
            result = client.transactions.export()
            assert result["status"] is True

    def test_partial_debit(self, client):
        with respx.mock:
            respx.post(f"{BASE}/transaction/partial_debit").mock(
                return_value=httpx.Response(200, json={"status": True, "data": {}})
            )
            result = client.transactions.partial_debit(
                authorization_code="AUTH_abc", email="test@example.com", amount=20.0, currency="NGN"
            )
            assert result["status"] is True

    def test_partial_debit_currency_not_hardcoded(self, client):
        with respx.mock:
            route = respx.post(f"{BASE}/transaction/partial_debit").mock(
                return_value=httpx.Response(200, json={"status": True, "data": {}})
            )
            client.transactions.partial_debit(
                authorization_code="AUTH_abc", email="test@example.com", amount=20.0, currency="USD"
            )
            import json
            body = json.loads(route.calls[0].request.content)
            assert body["currency"] == "USD"


class TestAsyncTransactions:
    async def test_initialize(self, async_client):
        with respx.mock:
            respx.post(f"{BASE}/transaction/initialize").mock(
                return_value=httpx.Response(200, json={"status": True, "data": {"authorization_url": "https://checkout.paystack.com/abc"}})
            )
            result = await async_client.transactions.initialize(email="test@example.com", amount=100.0, currency="GHS")
            assert result["status"] is True
        await async_client._client.close()

    async def test_verify(self, async_client):
        with respx.mock:
            respx.get(f"{BASE}/transaction/verify/ref123").mock(
                return_value=httpx.Response(200, json={"status": True, "data": {}})
            )
            result = await async_client.transactions.verify("ref123")
            assert result["status"] is True
        await async_client._client.close()
