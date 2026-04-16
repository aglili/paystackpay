import httpx

from .errors import (
    APIError,
    AuthenticationError,
    InvalidRequestError,
    NotFoundError,
    RateLimitError,
)

_STATUS_MAP = {
    401: AuthenticationError,
    400: InvalidRequestError,
    404: NotFoundError,
    429: RateLimitError,
}


def _raise_for_status(response: httpx.Response) -> dict:
    try:
        data = response.json()
    except Exception:
        data = {}

    if response.is_success:
        return data

    message = data.get("message", "An unexpected error occurred")
    exc_class = _STATUS_MAP.get(response.status_code, APIError)
    raise exc_class(message, status_code=response.status_code, raw_response=data)


class SyncClient:
    BASE_URL = "https://api.paystack.co"

    def __init__(self, secret_key: str) -> None:
        self._http = httpx.Client(
            base_url=self.BASE_URL,
            headers={"Authorization": f"Bearer {secret_key}"},
            timeout=30.0,
        )

    def request(self, method: str, endpoint: str, **kwargs) -> dict:
        response = self._http.request(method, endpoint, **kwargs)
        return _raise_for_status(response)

    def close(self) -> None:
        self._http.close()

    def __enter__(self):
        return self

    def __exit__(self, *args) -> None:
        self.close()


class AsyncClient:
    BASE_URL = "https://api.paystack.co"

    def __init__(self, secret_key: str) -> None:
        self._http = httpx.AsyncClient(
            base_url=self.BASE_URL,
            headers={"Authorization": f"Bearer {secret_key}"},
            timeout=30.0,
        )

    async def request(self, method: str, endpoint: str, **kwargs) -> dict:
        response = await self._http.request(method, endpoint, **kwargs)
        return _raise_for_status(response)

    async def close(self) -> None:
        await self._http.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args) -> None:
        await self.close()
