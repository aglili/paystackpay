from .._base import AsyncBaseResource, BaseResource
from ..utils import to_subunit


class Refunds(BaseResource):
    def create(
        self, transaction: str, amount: float | None = None, currency: str = "GHS", **kwargs
    ) -> dict:
        """Initiate a refund for a transaction. Omit amount to refund the full transaction value."""
        data: dict = {"transaction": transaction, **kwargs}
        if amount is not None:
            data["amount"] = to_subunit(amount, currency)
        return self._client.request("POST", "/refund", json=data)

    def list(self, **params) -> dict:
        """List all refunds on your integration."""
        return self._client.request("GET", "/refund", params=params)

    def fetch(self, refund_id: int | str) -> dict:
        """Fetch details of a specific refund by its ID."""
        return self._client.request("GET", f"/refund/{refund_id}")


class AsyncRefunds(AsyncBaseResource):
    async def create(
        self, transaction: str, amount: float | None = None, currency: str = "GHS", **kwargs
    ) -> dict:
        """Initiate a refund for a transaction. Omit amount to refund the full transaction value."""
        data: dict = {"transaction": transaction, **kwargs}
        if amount is not None:
            data["amount"] = to_subunit(amount, currency)
        return await self._client.request("POST", "/refund", json=data)

    async def list(self, **params) -> dict:
        """List all refunds on your integration."""
        return await self._client.request("GET", "/refund", params=params)

    async def fetch(self, refund_id: int | str) -> dict:
        """Fetch details of a specific refund by its ID."""
        return await self._client.request("GET", f"/refund/{refund_id}")
