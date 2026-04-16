from ._client import AsyncClient, SyncClient
from .errors import (
    APIError,
    AuthenticationError,
    InvalidRequestError,
    MissingSecretKeyError,
    NotFoundError,
    PaystackError,
    RateLimitError,
)
from .resources.customers import AsyncCustomers, Customers
from .resources.payment_requests import AsyncPaymentRequests, PaymentRequests
from .resources.plans import AsyncPlans, Plans
from .resources.refunds import AsyncRefunds, Refunds
from .resources.subaccounts import AsyncSubaccounts, Subaccounts
from .resources.transactions import AsyncTransactions, Transactions
from .resources.transfer_recipients import AsyncTransferRecipients, TransferRecipients
from .resources.transfers import AsyncTransfers, Transfers
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
