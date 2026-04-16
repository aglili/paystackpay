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


class TestSubaccounts:
    def test_create(self, client):
        with respx.mock:
            respx.post(f"{BASE}/subaccount").mock(
                return_value=httpx.Response(
                    200, json={"status": True, "data": {"subaccount_code": "ACCT_abc"}}
                )
            )
            result = client.subaccounts.create(
                business_name="Kofi Stores",
                settlement_bank="058",
                account_number="0123456789",
                percentage_charge=0.2,
            )
            assert result["status"] is True
            assert result["data"]["subaccount_code"] == "ACCT_abc"

    def test_list(self, client):
        with respx.mock:
            respx.get(f"{BASE}/subaccount").mock(
                return_value=httpx.Response(200, json={"status": True, "data": []})
            )
            result = client.subaccounts.list()
            assert result["status"] is True

    def test_fetch(self, client):
        with respx.mock:
            respx.get(f"{BASE}/subaccount/ACCT_abc").mock(
                return_value=httpx.Response(
                    200, json={"status": True, "data": {"subaccount_code": "ACCT_abc"}}
                )
            )
            result = client.subaccounts.fetch("ACCT_abc")
            assert result["data"]["subaccount_code"] == "ACCT_abc"

    def test_update(self, client):
        with respx.mock:
            respx.put(f"{BASE}/subaccount/ACCT_abc").mock(
                return_value=httpx.Response(200, json={"status": True, "data": {}})
            )
            result = client.subaccounts.update("ACCT_abc", business_name="New Name")
            assert result["status"] is True


class TestAsyncSubaccounts:
    async def test_create(self, async_client):
        with respx.mock:
            respx.post(f"{BASE}/subaccount").mock(
                return_value=httpx.Response(200, json={"status": True, "data": {}})
            )
            result = await async_client.subaccounts.create(
                business_name="Kofi Stores",
                settlement_bank="058",
                account_number="0123456789",
                percentage_charge=0.2,
            )
            assert result["status"] is True
        await async_client._client.close()
