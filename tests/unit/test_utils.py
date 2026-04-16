import pytest

from paystackpay.errors import InvalidRequestError
from paystackpay.utils import to_subunit, validate_amount


def test_to_subunit_ghs():
    assert to_subunit(100.0, "GHS") == 10000


def test_to_subunit_ngn():
    assert to_subunit(50.0, "NGN") == 5000


def test_to_subunit_usd():
    assert to_subunit(1.5, "USD") == 150


def test_to_subunit_lowercase_currency():
    assert to_subunit(100.0, "ghs") == 10000


def test_to_subunit_zero_is_valid():
    assert to_subunit(0, "NGN") == 0


def test_to_subunit_negative_raises():
    with pytest.raises(InvalidRequestError, match="negative"):
        to_subunit(-10.0, "NGN")


def test_to_subunit_none_raises():
    with pytest.raises(InvalidRequestError, match="required"):
        to_subunit(None, "NGN")


def test_to_subunit_string_raises():
    with pytest.raises(InvalidRequestError, match="number"):
        to_subunit("100", "NGN")


def test_validate_amount_valid():
    assert validate_amount(50.0) == 50.0


def test_validate_amount_zero():
    assert validate_amount(0) == 0


def test_validate_amount_negative_raises():
    with pytest.raises(InvalidRequestError):
        validate_amount(-1)


def test_validate_amount_none_raises():
    with pytest.raises(InvalidRequestError):
        validate_amount(None)


def test_validate_amount_string_raises():
    with pytest.raises(InvalidRequestError):
        validate_amount("fifty")
