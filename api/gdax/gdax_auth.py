import json
import hmac
import hashlib
import time
import base64
from requests.auth import AuthBase

from settings import GDAX_KEY, GDAX_SECRET, GDAX_PASSPHRASE


class GDAXAuth(AuthBase):
    def __init__(self):
        self.api_key = GDAX_KEY
        self.secret_key = GDAX_SECRET
        self.passphrase = GDAX_PASSPHRASE

    def __call__(self, request):
        timestamp = str(time.time())
        message = timestamp + request.method + request.path_url + (request.body or '')
        hmac_key = base64.b64decode(self.secret_key)
        signature = hmac.new(hmac_key, message.encode(), hashlib.sha256)
        signature_b64 = base64.b64encode(signature.digest()).decode()

        request.headers.update({
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
            'CB-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        })
        return request


GDAX_AUTH = GDAXAuth()
