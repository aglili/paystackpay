from .._base import AsyncBaseResource, BaseResource
from ..utils import to_subunit


class Transactions(BaseResource):
    def initialize(self, email: str, amount: float, currency: str = "GHS", **kwargs) -> dict:
        data = {
            "email": email,
            "amount": to_subunit(amount, currency),
            "currency": currency,
            **kwargs,
        }
        return self._client.request("POST", "/transaction/initialize", json=data)

    def verify(self, reference: str) -> dict:
        return self._client.request("GET", f"/transaction/verify/{reference}")

    def list(self, **params) -> dict:
        return self._client.request("GET", "/transaction", params=params)

    def fetch(self, transaction_id: int | str) -> dict:
        return self._client.request("GET", f"/transaction/{transaction_id}")

    def charge_authorization(
        self, email: str, amount: float, authorization_code: str, currency: str = "GHS", **kwargs
    ) -> dict:
        data = {
            "email": email,
            "amount": to_subunit(amount, currency),
            "authorization_code": authorization_code,
            **kwargs,
        }
        return self._client.request("POST", "/transaction/charge_authorization", json=data)

    def timeline(self, id_or_reference: str) -> dict:
        return self._client.request("GET", f"/transaction/timeline/{id_or_reference}")

    def totals(self, **params) -> dict:
        return self._client.request("GET", "/transaction/totals", params=params)

    def export(self, **params) -> dict:
        return self._client.request("GET", "/transaction/export", params=params)

    def partial_debit(
        self, authorization_code: str, email: str, amount: float, currency: str = "GHS"
    ) -> dict:
        data = {
            "authorization_code": authorization_code,
            "currency": currency,
            "email": email,
            "amount": to_subunit(amount, currency),
        }
        return self._client.request("POST", "/transaction/partial_debit", json=data)


class AsyncTransactions(AsyncBaseResource):
    async def initialize(self, email: str, amount: float, currency: str = "GHS", **kwargs) -> dict:
        data = {
            "email": email,
            "amount": to_subunit(amount, currency),
            "currency": currency,
            **kwargs,
        }
        return await self._client.request("POST", "/transaction/initialize", json=data)

    async def verify(self, reference: str) -> dict:
        return await self._client.request("GET", f"/transaction/verify/{reference}")

    async def list(self, **params) -> dict:
        return await self._client.request("GET", "/transaction", params=params)

    async def fetch(self, transaction_id: int | str) -> dict:
        return await self._client.request("GET", f"/transaction/{transaction_id}")

    async def charge_authorization(
        self, email: str, amount: float, authorization_code: str, currency: str = "GHS", **kwargs
    ) -> dict:
        data = {
            "email": email,
            "amount": to_subunit(amount, currency),
            "authorization_code": authorization_code,
            **kwargs,
        }
        return await self._client.request("POST", "/transaction/charge_authorization", json=data)

    async def timeline(self, id_or_reference: str) -> dict:
        return await self._client.request("GET", f"/transaction/timeline/{id_or_reference}")

    async def totals(self, **params) -> dict:
        return await self._client.request("GET", "/transaction/totals", params=params)

    async def export(self, **params) -> dict:
        return await self._client.request("GET", "/transaction/export", params=params)

    async def partial_debit(
        self, authorization_code: str, email: str, amount: float, currency: str = "GHS"
    ) -> dict:
        data = {
            "authorization_code": authorization_code,
            "currency": currency,
            "email": email,
            "amount": to_subunit(amount, currency),
        }
        return await self._client.request("POST", "/transaction/partial_debit", json=data)
