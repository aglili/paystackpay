from .._base import BaseResource, AsyncBaseResource


class Customers(BaseResource):
    def create(self, email: str, first_name: str, last_name: str, phone: str) -> dict:
        data = {"email": email, "first_name": first_name, "last_name": last_name, "phone": phone}
        return self._client.request("POST", "/customer", json=data)

    def list(self, **params) -> dict:
        return self._client.request("GET", "/customer", params=params)

    def fetch(self, email_or_code: str) -> dict:
        return self._client.request("GET", f"/customer/{email_or_code}")

    def update(self, customer_code: str, first_name: str | None = None, last_name: str | None = None, email: str | None = None, phone: str | None = None) -> dict:
        data = {}
        if first_name is not None:
            data["first_name"] = first_name
        if last_name is not None:
            data["last_name"] = last_name
        if email is not None:
            data["email"] = email
        if phone is not None:
            data["phone"] = phone
        return self._client.request("PUT", f"/customer/{customer_code}", json=data)

    def whitelist(self, customer_code: str) -> dict:
        data = {"customer": customer_code, "risk_action": "allow"}
        return self._client.request("POST", "/customer/set_risk_action", json=data)

    def blacklist(self, customer_code: str) -> dict:
        data = {"customer": customer_code, "risk_action": "deny"}
        return self._client.request("POST", "/customer/set_risk_action", json=data)

    def deactivate_authorization(self, authorization_code: str) -> dict:
        return self._client.request("POST", "/customer/deactivate_authorization", json={"authorization_code": authorization_code})


class AsyncCustomers(AsyncBaseResource):
    async def create(self, email: str, first_name: str, last_name: str, phone: str) -> dict:
        data = {"email": email, "first_name": first_name, "last_name": last_name, "phone": phone}
        return await self._client.request("POST", "/customer", json=data)

    async def list(self, **params) -> dict:
        return await self._client.request("GET", "/customer", params=params)

    async def fetch(self, email_or_code: str) -> dict:
        return await self._client.request("GET", f"/customer/{email_or_code}")

    async def update(self, customer_code: str, first_name: str | None = None, last_name: str | None = None, email: str | None = None, phone: str | None = None) -> dict:
        data = {}
        if first_name is not None:
            data["first_name"] = first_name
        if last_name is not None:
            data["last_name"] = last_name
        if email is not None:
            data["email"] = email
        if phone is not None:
            data["phone"] = phone
        return await self._client.request("PUT", f"/customer/{customer_code}", json=data)

    async def whitelist(self, customer_code: str) -> dict:
        data = {"customer": customer_code, "risk_action": "allow"}
        return await self._client.request("POST", "/customer/set_risk_action", json=data)

    async def blacklist(self, customer_code: str) -> dict:
        data = {"customer": customer_code, "risk_action": "deny"}
        return await self._client.request("POST", "/customer/set_risk_action", json=data)

    async def deactivate_authorization(self, authorization_code: str) -> dict:
        return await self._client.request("POST", "/customer/deactivate_authorization", json={"authorization_code": authorization_code})
