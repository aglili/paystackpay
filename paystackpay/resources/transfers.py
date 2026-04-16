from .._base import AsyncBaseResource, BaseResource
from ..utils import to_subunit


class Transfers(BaseResource):
    def initiate(self, amount: float, recipient: str, reason: str, currency: str = "NGN") -> dict:
        data = {
            "source": "balance",
            "amount": to_subunit(amount, currency),
            "recipient": recipient,
            "reason": reason,
        }
        return self._client.request("POST", "/transfer", json=data)

    def finalize(self, transfer_code: str, otp: str) -> dict:
        return self._client.request(
            "POST", "/transfer/finalize_transfer", json={"transfer_code": transfer_code, "otp": otp}
        )

    def fetch(self, id_or_code: str) -> dict:
        return self._client.request("GET", f"/transfer/{id_or_code}")

    def list(self, **params) -> dict:
        return self._client.request("GET", "/transfer", params=params)


class AsyncTransfers(AsyncBaseResource):
    async def initiate(
        self, amount: float, recipient: str, reason: str, currency: str = "NGN"
    ) -> dict:
        data = {
            "source": "balance",
            "amount": to_subunit(amount, currency),
            "recipient": recipient,
            "reason": reason,
        }
        return await self._client.request("POST", "/transfer", json=data)

    async def finalize(self, transfer_code: str, otp: str) -> dict:
        return await self._client.request(
            "POST", "/transfer/finalize_transfer", json={"transfer_code": transfer_code, "otp": otp}
        )

    async def fetch(self, id_or_code: str) -> dict:
        return await self._client.request("GET", f"/transfer/{id_or_code}")

    async def list(self, **params) -> dict:
        return await self._client.request("GET", "/transfer", params=params)
