from .._base import AsyncBaseResource, BaseResource


class TransferRecipients(BaseResource):
    def create(
        self,
        type: str,
        name: str,
        account_number: str,
        bank_code: str,
        currency: str = "GHS",
        **kwargs,
    ) -> dict:
        """Create a transfer recipient (bank account or mobile money). type is typically 'ghipss' or 'nuban'."""
        data = {
            "type": type,
            "name": name,
            "account_number": account_number,
            "bank_code": bank_code,
            "currency": currency,
            **kwargs,
        }
        return self._client.request("POST", "/transferrecipient", json=data)

    def list(self, **params) -> dict:
        """List all transfer recipients on your integration."""
        return self._client.request("GET", "/transferrecipient", params=params)

    def fetch(self, id_or_code: str) -> dict:
        """Fetch details of a transfer recipient by ID or recipient code."""
        return self._client.request("GET", f"/transferrecipient/{id_or_code}")

    def update(self, id_or_code: str, name: str | None = None, email: str | None = None) -> dict:
        """Update the name or email of a transfer recipient."""
        data = {}
        if name is not None:
            data["name"] = name
        if email is not None:
            data["email"] = email
        return self._client.request("PUT", f"/transferrecipient/{id_or_code}", json=data)

    def delete(self, id_or_code: str) -> dict:
        """Delete a transfer recipient, preventing further transfers to them."""
        return self._client.request("DELETE", f"/transferrecipient/{id_or_code}")


class AsyncTransferRecipients(AsyncBaseResource):
    async def create(
        self,
        type: str,
        name: str,
        account_number: str,
        bank_code: str,
        currency: str = "GHS",
        **kwargs,
    ) -> dict:
        """Create a transfer recipient (bank account or mobile money). type is typically 'ghipss' or 'nuban'."""
        data = {
            "type": type,
            "name": name,
            "account_number": account_number,
            "bank_code": bank_code,
            "currency": currency,
            **kwargs,
        }
        return await self._client.request("POST", "/transferrecipient", json=data)

    async def list(self, **params) -> dict:
        """List all transfer recipients on your integration."""
        return await self._client.request("GET", "/transferrecipient", params=params)

    async def fetch(self, id_or_code: str) -> dict:
        """Fetch details of a transfer recipient by ID or recipient code."""
        return await self._client.request("GET", f"/transferrecipient/{id_or_code}")

    async def update(
        self, id_or_code: str, name: str | None = None, email: str | None = None
    ) -> dict:
        """Update the name or email of a transfer recipient."""
        data = {}
        if name is not None:
            data["name"] = name
        if email is not None:
            data["email"] = email
        return await self._client.request("PUT", f"/transferrecipient/{id_or_code}", json=data)

    async def delete(self, id_or_code: str) -> dict:
        """Delete a transfer recipient, preventing further transfers to them."""
        return await self._client.request("DELETE", f"/transferrecipient/{id_or_code}")
