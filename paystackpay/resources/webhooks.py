import hashlib
import hmac


class Webhooks:
    def verify_signature(self, payload: bytes, signature: str, secret: str) -> bool:
        expected = hmac.new(secret.encode(), payload, hashlib.sha512).hexdigest()
        return hmac.compare_digest(expected, signature)
