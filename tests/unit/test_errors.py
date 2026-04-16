from paystackpay.errors import (
    PaystackError,
    AuthenticationError,
    InvalidRequestError,
    NotFoundError,
    RateLimitError,
    APIError,
    MissingSecretKeyError,
)


def test_paystack_error_base():
    err = PaystackError("something went wrong", status_code=500, raw_response={"message": "err"})
    assert str(err) == "something went wrong"
    assert err.status_code == 500
    assert err.raw_response == {"message": "err"}


def test_paystack_error_defaults():
    err = PaystackError("oops")
    assert err.status_code is None
    assert err.raw_response == {}


def test_authentication_error_is_paystack_error():
    err = AuthenticationError("Invalid key", status_code=401, raw_response={})
    assert isinstance(err, PaystackError)
    assert err.status_code == 401


def test_invalid_request_error():
    err = InvalidRequestError("Bad param", status_code=400, raw_response={"field": "email"})
    assert isinstance(err, PaystackError)
    assert err.raw_response["field"] == "email"


def test_not_found_error():
    err = NotFoundError("Not found", status_code=404, raw_response={})
    assert isinstance(err, PaystackError)


def test_rate_limit_error():
    err = RateLimitError("Too many requests", status_code=429, raw_response={})
    assert isinstance(err, PaystackError)


def test_api_error():
    err = APIError("Server error", status_code=500, raw_response={})
    assert isinstance(err, PaystackError)


def test_missing_secret_key_error():
    err = MissingSecretKeyError("secret_key is required")
    assert isinstance(err, PaystackError)
