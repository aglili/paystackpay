from .._base import AsyncBaseResource, BaseResource


class Subaccounts(BaseResource):
    def create(
        self,
        business_name: str,
        settlement_bank: str,
        account_number: str,
        percentage_charge: float,
        **kwargs,
    ) -> dict:
        """Create a subaccount to enable split payments. percentage_charge is between 0 and 100."""
        data = {
            "business_name": business_name,
            "settlement_bank": settlement_bank,
            "account_number": account_number,
            "percentage_charge": percentage_charge,
            **kwargs,
        }
        return self._client.request("POST", "/subaccount", json=data)

    def list(self, **params) -> dict:
        """List all subaccounts on your integration."""
        return self._client.request("GET", "/subaccount", params=params)

    def fetch(self, id_or_code: str) -> dict:
        """Fetch details of a subaccount by its ID or subaccount code."""
        return self._client.request("GET", f"/subaccount/{id_or_code}")

    def update(self, id_or_code: str, **kwargs) -> dict:
        """Update details of a subaccount. Pass any updatable fields as keyword arguments."""
        return self._client.request("PUT", f"/subaccount/{id_or_code}", json=kwargs)


class AsyncSubaccounts(AsyncBaseResource):
    async def create(
        self,
        business_name: str,
        settlement_bank: str,
        account_number: str,
        percentage_charge: float,
        **kwargs,
    ) -> dict:
        """Create a subaccount to enable split payments. percentage_charge is between 0 and 100."""
        data = {
            "business_name": business_name,
            "settlement_bank": settlement_bank,
            "account_number": account_number,
            "percentage_charge": percentage_charge,
            **kwargs,
        }
        return await self._client.request("POST", "/subaccount", json=data)

    async def list(self, **params) -> dict:
        """List all subaccounts on your integration."""
        return await self._client.request("GET", "/subaccount", params=params)

    async def fetch(self, id_or_code: str) -> dict:
        """Fetch details of a subaccount by its ID or subaccount code."""
        return await self._client.request("GET", f"/subaccount/{id_or_code}")

    async def update(self, id_or_code: str, **kwargs) -> dict:
        """Update details of a subaccount. Pass any updatable fields as keyword arguments."""
        return await self._client.request("PUT", f"/subaccount/{id_or_code}", json=kwargs)
