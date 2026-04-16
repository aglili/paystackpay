from .._base import BaseResource, AsyncBaseResource
from ..utils import to_subunit


class Refunds(BaseResource):
    def create(self, transaction: str, amount: float | None = None, currency: str = "NGN", **kwargs) -> dict:
        data: dict = {"transaction": transaction, **kwargs}
        if amount is not None:
            data["amount"] = to_subunit(amount, currency)
        return self._client.request("POST", "/refund", json=data)

    def list(self, **params) -> dict:
        return self._client.request("GET", "/refund", params=params)

    def fetch(self, refund_id: int | str) -> dict:
        return self._client.request("GET", f"/refund/{refund_id}")


class AsyncRefunds(AsyncBaseResource):
    async def create(self, transaction: str, amount: float | None = None, currency: str = "NGN", **kwargs) -> dict:
        data: dict = {"transaction": transaction, **kwargs}
        if amount is not None:
            data["amount"] = to_subunit(amount, currency)
        return await self._client.request("POST", "/refund", json=data)

    async def list(self, **params) -> dict:
        return await self._client.request("GET", "/refund", params=params)

    async def fetch(self, refund_id: int | str) -> dict:
        return await self._client.request("GET", f"/refund/{refund_id}")
