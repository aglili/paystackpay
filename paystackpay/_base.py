from ._client import AsyncClient, SyncClient


class BaseResource:
    def __init__(self, client: SyncClient) -> None:
        self._client = client


class AsyncBaseResource:
    def __init__(self, client: AsyncClient) -> None:
        self._client = client
