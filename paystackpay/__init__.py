from ._client import SyncClient, AsyncClient
from ._base import BaseResource, AsyncBaseResource
from .errors import (
    PaystackError,
    AuthenticationError,
    InvalidRequestError,
    NotFoundError,
    RateLimitError,
    APIError,
    MissingSecretKeyError,
)
from .resources.transactions import Transactions, AsyncTransactions
from .resources.customers import Customers, AsyncCustomers
from .resources.plans import Plans, AsyncPlans
from .resources.transfers import Transfers, AsyncTransfers
from .resources.transfer_recipients import TransferRecipients, AsyncTransferRecipients
from .resources.payment_requests import PaymentRequests, AsyncPaymentRequests
from .resources.refunds import Refunds, AsyncRefunds
from .resources.subaccounts import Subaccounts, AsyncSubaccounts
from .resources.webhooks import Webhooks

__version__ = "1.0.0"

__all__ = [
    "Paystack",
    "AsyncPaystack",
    "PaystackError",
    "AuthenticationError",
    "InvalidRequestError",
    "NotFoundError",
    "RateLimitError",
    "APIError",
    "MissingSecretKeyError",
]


class Paystack:
    def __init__(self, secret_key: str) -> None:
        if not secret_key:
            raise MissingSecretKeyError("secret_key is required")
        self._client = SyncClient(secret_key)
        self.transactions = Transactions(self._client)
        self.customers = Customers(self._client)
        self.plans = Plans(self._client)
        self.transfers = Transfers(self._client)
        self.transfer_recipients = TransferRecipients(self._client)
        self.payment_requests = PaymentRequests(self._client)
        self.refunds = Refunds(self._client)
        self.subaccounts = Subaccounts(self._client)
        self.webhooks = Webhooks()

    def __enter__(self):
        return self

    def __exit__(self, *args) -> None:
        self._client.close()


class AsyncPaystack:
    def __init__(self, secret_key: str) -> None:
        if not secret_key:
            raise MissingSecretKeyError("secret_key is required")
        self._client = AsyncClient(secret_key)
        self.transactions = AsyncTransactions(self._client)
        self.customers = AsyncCustomers(self._client)
        self.plans = AsyncPlans(self._client)
        self.transfers = AsyncTransfers(self._client)
        self.transfer_recipients = AsyncTransferRecipients(self._client)
        self.payment_requests = AsyncPaymentRequests(self._client)
        self.refunds = AsyncRefunds(self._client)
        self.subaccounts = AsyncSubaccounts(self._client)
        self.webhooks = Webhooks()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args) -> None:
        await self._client.close()
