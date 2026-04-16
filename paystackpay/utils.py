from .errors import InvalidRequestError

_SUBUNIT_MULTIPLIERS: dict[str, int] = {
    "GHS": 100,
    "NGN": 100,
    "USD": 100,
    "ZAR": 100,
    "KES": 100,
}


def to_subunit(amount: float, currency: str) -> int:
    if amount is None:
        raise InvalidRequestError("Amount is required")
    if not isinstance(amount, (int, float)):
        raise InvalidRequestError("Amount must be a number")
    if amount < 0:
        raise InvalidRequestError("Amount must not be negative")
    multiplier = _SUBUNIT_MULTIPLIERS.get(currency.upper(), 100)
    return int(amount * multiplier)


def validate_amount(amount: float) -> float:
    if amount is None:
        raise InvalidRequestError("Amount is required")
    if not isinstance(amount, (int, float)):
        raise InvalidRequestError("Amount must be a number")
    if amount < 0:
        raise InvalidRequestError("Amount must not be negative")
    return amount
