import os
import pytest


pytestmark = pytest.mark.skipif(
    not os.getenv("PAYSTACK_TEST_KEY"),
    reason="Set PAYSTACK_TEST_KEY to run integration tests"
)


class TestTransactionsIntegration:
    def test_initialize_transaction(self, client):
        result = client.transactions.initialize(
            email="test@example.com", amount=10.0, currency="GHS"
        )
        assert result["status"] is True
        assert "authorization_url" in result["data"]

    async def test_async_initialize_transaction(self, async_client):
        result = await async_client.transactions.initialize(
            email="test@example.com", amount=10.0, currency="GHS"
        )
        assert result["status"] is True
        await async_client._client.close()
