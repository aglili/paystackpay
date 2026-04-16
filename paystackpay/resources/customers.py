from .._base import AsyncBaseResource, BaseResource


class Customers(BaseResource):
    def create(self, email: str, first_name: str, last_name: str, phone: str) -> dict:
        """Create a new customer on your integration."""
        data = {"email": email, "first_name": first_name, "last_name": last_name, "phone": phone}
        return self._client.request("POST", "/customer", json=data)

    def list(self, **params) -> dict:
        """List all customers on your integration."""
        return self._client.request("GET", "/customer", params=params)

    def fetch(self, email_or_code: str) -> dict:
        """Fetch details of a customer by their email address or customer code."""
        return self._client.request("GET", f"/customer/{email_or_code}")

    def update(
        self,
        customer_code: str,
        first_name: str | None = None,
        last_name: str | None = None,
        email: str | None = None,
        phone: str | None = None,
    ) -> dict:
        """Update details of an existing customer. Only provided fields are updated."""
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
        """Whitelist a customer, allowing them to make transactions."""
        data = {"customer": customer_code, "risk_action": "allow"}
        return self._client.request("POST", "/customer/set_risk_action", json=data)

    def blacklist(self, customer_code: str) -> dict:
        """Blacklist a customer, blocking them from making transactions."""
        data = {"customer": customer_code, "risk_action": "deny"}
        return self._client.request("POST", "/customer/set_risk_action", json=data)

    def deactivate_authorization(self, authorization_code: str) -> dict:
        """Deactivate a saved card authorization so it can no longer be charged."""
        return self._client.request(
            "POST",
            "/customer/deactivate_authorization",
            json={"authorization_code": authorization_code},
        )


class AsyncCustomers(AsyncBaseResource):
    async def create(self, email: str, first_name: str, last_name: str, phone: str) -> dict:
        """Create a new customer on your integration."""
        data = {"email": email, "first_name": first_name, "last_name": last_name, "phone": phone}
        return await self._client.request("POST", "/customer", json=data)

    async def list(self, **params) -> dict:
        """List all customers on your integration."""
        return await self._client.request("GET", "/customer", params=params)

    async def fetch(self, email_or_code: str) -> dict:
        """Fetch details of a customer by their email address or customer code."""
        return await self._client.request("GET", f"/customer/{email_or_code}")

    async def update(
        self,
        customer_code: str,
        first_name: str | None = None,
        last_name: str | None = None,
        email: str | None = None,
        phone: str | None = None,
    ) -> dict:
        """Update details of an existing customer. Only provided fields are updated."""
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
        """Whitelist a customer, allowing them to make transactions."""
        data = {"customer": customer_code, "risk_action": "allow"}
        return await self._client.request("POST", "/customer/set_risk_action", json=data)

    async def blacklist(self, customer_code: str) -> dict:
        """Blacklist a customer, blocking them from making transactions."""
        data = {"customer": customer_code, "risk_action": "deny"}
        return await self._client.request("POST", "/customer/set_risk_action", json=data)

    async def deactivate_authorization(self, authorization_code: str) -> dict:
        """Deactivate a saved card authorization so it can no longer be charged."""
        return await self._client.request(
            "POST",
            "/customer/deactivate_authorization",
            json={"authorization_code": authorization_code},
        )
