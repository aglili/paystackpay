from .._base import AsyncBaseResource, BaseResource
from ..utils import to_subunit


class PaymentRequests(BaseResource):
    def create(
        self, customer: str, description: str, amount: float, currency: str = "GHS", **kwargs
    ) -> dict:
        """Create a payment request and send it to a customer for them to pay."""
        data = {
            "customer": customer,
            "description": description,
            "amount": to_subunit(amount, currency),
            "currency": currency,
            **kwargs,
        }
        return self._client.request("POST", "/paymentrequest", json=data)

    def fetch(self, id_or_code: str) -> dict:
        """Fetch details of a payment request by its ID or request code."""
        return self._client.request("GET", f"/paymentrequest/{id_or_code}")

    def list(self, **params) -> dict:
        """List all payment requests on your integration."""
        return self._client.request("GET", "/paymentrequest", params=params)

    def verify(self, id_or_code: str) -> dict:
        """Verify a payment request to confirm whether it has been paid."""
        return self._client.request("GET", f"/paymentrequest/verify/{id_or_code}")

    def send_notification(self, id_or_code: str) -> dict:
        """Resend a notification email for a payment request to the customer."""
        return self._client.request("POST", f"/paymentrequest/notify/{id_or_code}")


class AsyncPaymentRequests(AsyncBaseResource):
    async def create(
        self, customer: str, description: str, amount: float, currency: str = "GHS", **kwargs
    ) -> dict:
        """Create a payment request and send it to a customer for them to pay."""
        data = {
            "customer": customer,
            "description": description,
            "amount": to_subunit(amount, currency),
            "currency": currency,
            **kwargs,
        }
        return await self._client.request("POST", "/paymentrequest", json=data)

    async def fetch(self, id_or_code: str) -> dict:
        """Fetch details of a payment request by its ID or request code."""
        return await self._client.request("GET", f"/paymentrequest/{id_or_code}")

    async def list(self, **params) -> dict:
        """List all payment requests on your integration."""
        return await self._client.request("GET", "/paymentrequest", params=params)

    async def verify(self, id_or_code: str) -> dict:
        """Verify a payment request to confirm whether it has been paid."""
        return await self._client.request("GET", f"/paymentrequest/verify/{id_or_code}")

    async def send_notification(self, id_or_code: str) -> dict:
        """Resend a notification email for a payment request to the customer."""
        return await self._client.request("POST", f"/paymentrequest/notify/{id_or_code}")
