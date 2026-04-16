from .._base import AsyncBaseResource, BaseResource
from ..utils import to_subunit


class Plans(BaseResource):
    def create(self, name: str, interval: str, amount: float, currency: str = "GHS") -> dict:
        """Create a subscription plan. interval must be one of: hourly, daily, weekly, monthly, annually."""
        data = {
            "name": name,
            "interval": interval,
            "amount": to_subunit(amount, currency),
            "currency": currency,
        }
        return self._client.request("POST", "/plan", json=data)

    def list(self, **params) -> dict:
        """List all subscription plans on your integration."""
        return self._client.request("GET", "/plan", params=params)

    def fetch(self, id_or_code: str) -> dict:
        """Fetch details of a subscription plan by its ID or plan code."""
        return self._client.request("GET", f"/plan/{id_or_code}")

    def update(
        self,
        id_or_code: str,
        name: str | None = None,
        interval: str | None = None,
        amount: float | None = None,
        currency: str = "GHS",
    ) -> dict:
        """Update a subscription plan. Only provided fields are changed."""
        data = {}
        if name is not None:
            data["name"] = name
        if interval is not None:
            data["interval"] = interval
        if amount is not None:
            data["amount"] = to_subunit(amount, currency)
        return self._client.request("PUT", f"/plan/{id_or_code}", json=data)


class AsyncPlans(AsyncBaseResource):
    async def create(self, name: str, interval: str, amount: float, currency: str = "GHS") -> dict:
        """Create a subscription plan. interval must be one of: hourly, daily, weekly, monthly, annually."""
        data = {
            "name": name,
            "interval": interval,
            "amount": to_subunit(amount, currency),
            "currency": currency,
        }
        return await self._client.request("POST", "/plan", json=data)

    async def list(self, **params) -> dict:
        """List all subscription plans on your integration."""
        return await self._client.request("GET", "/plan", params=params)

    async def fetch(self, id_or_code: str) -> dict:
        """Fetch details of a subscription plan by its ID or plan code."""
        return await self._client.request("GET", f"/plan/{id_or_code}")

    async def update(
        self,
        id_or_code: str,
        name: str | None = None,
        interval: str | None = None,
        amount: float | None = None,
        currency: str = "GHS",
    ) -> dict:
        """Update a subscription plan. Only provided fields are changed."""
        data = {}
        if name is not None:
            data["name"] = name
        if interval is not None:
            data["interval"] = interval
        if amount is not None:
            data["amount"] = to_subunit(amount, currency)
        return await self._client.request("PUT", f"/plan/{id_or_code}", json=data)
