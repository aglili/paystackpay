# paystackpay

A Python wrapper for the [Paystack](https://paystack.com) API. Supports both sync and async usage.

## Installation

```bash
pip install paystackpay
```

## Quickstart

```python
from paystackpay import Paystack

client = Paystack(secret_key="sk_live_...")

# Initialize a transaction
response = client.transactions.initialize(
    email="customer@example.com",
    amount=100.0,  # GHS 100 — pass amounts in major units
    currency="GHS",
)
print(response["data"]["authorization_url"])
```

### Async

```python
import asyncio
from paystackpay import AsyncPaystack

async def main():
    client = AsyncPaystack(secret_key="sk_live_...")
    response = await client.transactions.initialize(
        email="customer@example.com",
        amount=100.0,
        currency="GHS",
    )
    print(response["data"]["authorization_url"])

asyncio.run(main())
```

### Context managers

```python
# Sync
with Paystack(secret_key="sk_live_...") as client:
    client.transactions.list()

# Async
async with AsyncPaystack(secret_key="sk_live_...") as client:
    await client.transactions.list()
```

## Amounts

Pass amounts in the **major currency unit** (e.g. `100.0` = GHS 100 / NGN 100). The library converts to the subunit (pesewas/kobo) before sending to Paystack.

## Resources

All resources are available as attributes on the client. Every sync method has an identical async counterpart on `AsyncPaystack`.

### Transactions

```python
client.transactions.initialize(email, amount, currency)
client.transactions.verify(reference)
client.transactions.list()
client.transactions.fetch(transaction_id)
client.transactions.charge_authorization(email, amount, authorization_code, currency)
client.transactions.timeline(id_or_reference)
client.transactions.totals()
client.transactions.export()
client.transactions.partial_debit(authorization_code, email, amount, currency)
```

### Customers

```python
client.customers.create(email, first_name, last_name, phone)
client.customers.list()
client.customers.fetch(email_or_code)
client.customers.update(customer_code, first_name=None, last_name=None, email=None, phone=None)
client.customers.whitelist(customer_code)
client.customers.blacklist(customer_code)
client.customers.deactivate_authorization(authorization_code)
```

### Plans

```python
client.plans.create(name, interval, amount, currency)
client.plans.list()
client.plans.fetch(id_or_code)
client.plans.update(id_or_code, name=None, interval=None, amount=None)
```

### Transfers

```python
client.transfers.initiate(amount, recipient, reason, currency)
client.transfers.finalize(transfer_code, otp)
client.transfers.fetch(id_or_code)
client.transfers.list()
```

### Transfer Recipients

```python
client.transfer_recipients.create(type, name, account_number, bank_code, currency)
client.transfer_recipients.list()
client.transfer_recipients.fetch(id_or_code)
client.transfer_recipients.update(id_or_code, name=None, email=None)
client.transfer_recipients.delete(id_or_code)
```

### Payment Requests

```python
client.payment_requests.create(customer, description, amount, currency)
client.payment_requests.fetch(id_or_code)
client.payment_requests.list()
client.payment_requests.verify(id_or_code)
client.payment_requests.send_notification(id_or_code)
```

### Refunds

```python
client.refunds.create(transaction, amount=None, currency="NGN")
client.refunds.list()
client.refunds.fetch(refund_id)
```

### Subaccounts

```python
client.subaccounts.create(business_name, settlement_bank, account_number, percentage_charge)
client.subaccounts.list()
client.subaccounts.fetch(id_or_code)
client.subaccounts.update(id_or_code, **kwargs)
```

### Webhooks

Verify the `x-paystack-signature` header on incoming webhook events — no HTTP call made.

```python
payload = request.body  # raw bytes
signature = request.headers["x-paystack-signature"]

is_valid = client.webhooks.verify_signature(payload, signature, secret="your_webhook_secret")

if not is_valid:
    return HttpResponse(status=400)
```

## Error Handling

All errors are subclasses of `PaystackError` and carry `.message`, `.status_code`, and `.raw_response`.

```python
from paystackpay import Paystack, AuthenticationError, InvalidRequestError, PaystackError

client = Paystack(secret_key="sk_live_...")

try:
    client.transactions.initialize(email="bad", amount=100.0, currency="NGN")
except AuthenticationError as e:
    print(f"Bad key: {e.message}")
except InvalidRequestError as e:
    print(f"Bad params: {e.message} — {e.raw_response}")
except PaystackError as e:
    print(f"Paystack error {e.status_code}: {e.message}")
```

| Exception | Status code |
|---|---|
| `AuthenticationError` | 401 |
| `InvalidRequestError` | 400 |
| `NotFoundError` | 404 |
| `RateLimitError` | 429 |
| `APIError` | 5xx |

## Requirements

- Python 3.10+
- `httpx`
- `pydantic`

## License

MIT
