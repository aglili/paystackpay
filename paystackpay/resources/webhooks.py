import hashlib
import hmac


class Webhooks:
    def verify_signature(self, payload: bytes, signature: str, secret: str) -> bool:
        """Verify a Paystack webhook signature using HMAC-SHA512. Returns True if the signature is valid."""
        expected = hmac.new(secret.encode(), payload, hashlib.sha512).hexdigest()
        return hmac.compare_digest(expected, signature)
