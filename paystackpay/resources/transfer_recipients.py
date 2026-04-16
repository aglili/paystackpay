from .._base import AsyncBaseResource, BaseResource


class TransferRecipients(BaseResource):
    def create(
        self,
        type: str,
        name: str,
        account_number: str,
        bank_code: str,
        currency: str = "NGN",
        **kwargs,
    ) -> dict:
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
        return self._client.request("GET", "/transferrecipient", params=params)

    def fetch(self, id_or_code: str) -> dict:
        return self._client.request("GET", f"/transferrecipient/{id_or_code}")

    def update(self, id_or_code: str, name: str | None = None, email: str | None = None) -> dict:
        data = {}
        if name is not None:
            data["name"] = name
        if email is not None:
            data["email"] = email
        return self._client.request("PUT", f"/transferrecipient/{id_or_code}", json=data)

    def delete(self, id_or_code: str) -> dict:
        return self._client.request("DELETE", f"/transferrecipient/{id_or_code}")


class AsyncTransferRecipients(AsyncBaseResource):
    async def create(
        self,
        type: str,
        name: str,
        account_number: str,
        bank_code: str,
        currency: str = "NGN",
        **kwargs,
    ) -> dict:
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
        return await self._client.request("GET", "/transferrecipient", params=params)

    async def fetch(self, id_or_code: str) -> dict:
        return await self._client.request("GET", f"/transferrecipient/{id_or_code}")

    async def update(
        self, id_or_code: str, name: str | None = None, email: str | None = None
    ) -> dict:
        data = {}
        if name is not None:
            data["name"] = name
        if email is not None:
            data["email"] = email
        return await self._client.request("PUT", f"/transferrecipient/{id_or_code}", json=data)

    async def delete(self, id_or_code: str) -> dict:
        return await self._client.request("DELETE", f"/transferrecipient/{id_or_code}")
