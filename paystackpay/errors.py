class PaystackError(Exception):
    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        raw_response: dict | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.raw_response = raw_response or {}


class AuthenticationError(PaystackError):
    pass


class InvalidRequestError(PaystackError):
    pass


class NotFoundError(PaystackError):
    pass


class RateLimitError(PaystackError):
    pass


class APIError(PaystackError):
    pass


class MissingSecretKeyError(PaystackError):
    pass

