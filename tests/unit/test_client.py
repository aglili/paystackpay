import httpx
import pytest
import respx

from paystackpay._client import AsyncClient, SyncClient
from paystackpay.errors import (
    APIError,
    AuthenticationError,
    InvalidRequestError,
    NotFoundError,
    RateLimitError,
)

BASE = "https://api.paystack.co"


class TestSyncClient:
    def test_successful_response(self):
        client = SyncClient("sk_test_123")
        with respx.mock:
            respx.get(f"{BASE}/test").mock(
                return_value=httpx.Response(200, json={"status": True, "data": {}})
            )
            result = client.request("GET", "/test")
            assert result["status"] is True

    def test_401_raises_authentication_error(self):
        client = SyncClient("sk_test_bad")
        with respx.mock:
            respx.get(f"{BASE}/test").mock(
                return_value=httpx.Response(401, json={"message": "Invalid key"})
            )
            with pytest.raises(AuthenticationError) as exc_info:
                client.request("GET", "/test")
            assert exc_info.value.status_code == 401
            assert "Invalid key" in exc_info.value.message

    def test_400_raises_invalid_request_error(self):
        client = SyncClient("sk_test_123")
        with respx.mock:
            respx.post(f"{BASE}/test").mock(
                return_value=httpx.Response(400, json={"message": "email is required"})
            )
            with pytest.raises(InvalidRequestError) as exc_info:
                client.request("POST", "/test", json={})
            assert exc_info.value.status_code == 400

    def test_404_raises_not_found_error(self):
        client = SyncClient("sk_test_123")
        with respx.mock:
            respx.get(f"{BASE}/test/missing").mock(
                return_value=httpx.Response(404, json={"message": "Not found"})
            )
            with pytest.raises(NotFoundError):
                client.request("GET", "/test/missing")

    def test_429_raises_rate_limit_error(self):
        client = SyncClient("sk_test_123")
        with respx.mock:
            respx.get(f"{BASE}/test").mock(
                return_value=httpx.Response(429, json={"message": "Too many requests"})
            )
            with pytest.raises(RateLimitError):
                client.request("GET", "/test")

    def test_500_raises_api_error(self):
        client = SyncClient("sk_test_123")
        with respx.mock:
            respx.get(f"{BASE}/test").mock(
                return_value=httpx.Response(500, json={"message": "Internal server error"})
            )
            with pytest.raises(APIError):
                client.request("GET", "/test")

    def test_context_manager(self):
        with SyncClient("sk_test_123") as client:
            assert client is not None


class TestAsyncClient:
    async def test_successful_response(self):
        client = AsyncClient("sk_test_123")
        with respx.mock:
            respx.get(f"{BASE}/test").mock(
                return_value=httpx.Response(200, json={"status": True, "data": {}})
            )
            result = await client.request("GET", "/test")
            assert result["status"] is True
        await client.close()

    async def test_401_raises_authentication_error(self):
        client = AsyncClient("sk_test_bad")
        with respx.mock:
            respx.get(f"{BASE}/test").mock(
                return_value=httpx.Response(401, json={"message": "Invalid key"})
            )
            with pytest.raises(AuthenticationError):
                await client.request("GET", "/test")
        await client.close()

    async def test_async_context_manager(self):
        async with AsyncClient("sk_test_123") as client:
            assert client is not None
