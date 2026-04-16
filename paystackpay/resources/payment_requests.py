from .._base import BaseResource, AsyncBaseResource
from ..utils import to_subunit


class PaymentRequests(BaseResource):
    def create(self, customer: str, description: str, amount: float, currency: str = "NGN", **kwargs) -> dict:
        data = {"customer": customer, "description": description, "amount": to_subunit(amount, currency), "currency": currency, **kwargs}
        return self._client.request("POST", "/paymentrequest", json=data)

    def fetch(self, id_or_code: str) -> dict:
        return self._client.request("GET", f"/paymentrequest/{id_or_code}")

    def list(self, **params) -> dict:
        return self._client.request("GET", "/paymentrequest", params=params)

    def verify(self, id_or_code: str) -> dict:
        return self._client.request("GET", f"/paymentrequest/verify/{id_or_code}")

    def send_notification(self, id_or_code: str) -> dict:
        return self._client.request("POST", f"/paymentrequest/notify/{id_or_code}")


class AsyncPaymentRequests(AsyncBaseResource):
    async def create(self, customer: str, description: str, amount: float, currency: str = "NGN", **kwargs) -> dict:
        data = {"customer": customer, "description": description, "amount": to_subunit(amount, currency), "currency": currency, **kwargs}
        return await self._client.request("POST", "/paymentrequest", json=data)

    async def fetch(self, id_or_code: str) -> dict:
        return await self._client.request("GET", f"/paymentrequest/{id_or_code}")

    async def list(self, **params) -> dict:
        return await self._client.request("GET", "/paymentrequest", params=params)

    async def verify(self, id_or_code: str) -> dict:
        return await self._client.request("GET", f"/paymentrequest/verify/{id_or_code}")

    async def send_notification(self, id_or_code: str) -> dict:
        return await self._client.request("POST", f"/paymentrequest/notify/{id_or_code}")
