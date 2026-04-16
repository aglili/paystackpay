import hashlib
import hmac
import pytest
from paystackpay import Paystack

SECRET = "whsec_test_secret"

@pytest.fixture
def client():
    return Paystack(secret_key="sk_test_123")

def make_signature(payload: bytes, secret: str) -> str:
    return hmac.new(secret.encode(), payload, hashlib.sha512).hexdigest()

class TestWebhooks:
    def test_valid_signature_returns_true(self, client):
        payload = b'{"event":"charge.success","data":{}}'
        sig = make_signature(payload, SECRET)
        assert client.webhooks.verify_signature(payload, sig, SECRET) is True

    def test_invalid_signature_returns_false(self, client):
        payload = b'{"event":"charge.success","data":{}}'
        assert client.webhooks.verify_signature(payload, "badsignature", SECRET) is False

    def test_tampered_payload_returns_false(self, client):
        payload = b'{"event":"charge.success","data":{}}'
        sig = make_signature(payload, SECRET)
        tampered = b'{"event":"charge.success","data":{"tampered":true}}'
        assert client.webhooks.verify_signature(tampered, sig, SECRET) is False

    def test_wrong_secret_returns_false(self, client):
        payload = b'{"event":"charge.success","data":{}}'
        sig = make_signature(payload, SECRET)
        assert client.webhooks.verify_signature(payload, sig, "wrong_secret") is False

    def test_webhooks_has_no_client(self, client):
        assert not hasattr(client.webhooks, "_client")
