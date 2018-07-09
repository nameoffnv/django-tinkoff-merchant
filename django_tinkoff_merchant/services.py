import hashlib
import json
import types

import requests

from .utils import Encoder
from .models import Payment
from .settings import get_config


class PaymentHTTPException(Exception):
    pass


class MerchantAPI:
    _terminal_key = None
    _secret_key = None

    def __init__(self, terminal_key: str = None, secret_key: str = None):
        self._terminal_key = terminal_key
        self._secret_key = secret_key

    @property
    def secret_key(self):
        if not self._secret_key:
            self._secret_key = get_config()['SECRET_KEY']
        return self._secret_key

    @property
    def terminal_key(self):
        if not self._terminal_key:
            self._terminal_key = get_config()['TERMINAL_KEY']
        return self._terminal_key

    def _request(self, url: str, method: types.FunctionType, data: dict) -> requests.Response:
        url = get_config()['URLS'][url]

        data.update({
            'TerminalKey': self.terminal_key,
            'Token': self._token(data),
        })

        r = method(url, data=json.dumps(data, cls=Encoder), headers={'Content-Type': 'application/json'})

        if r.status_code != 200:
            raise PaymentHTTPException('bad status code')

        return r

    def _token(self, data: dict) -> str:
        base = [
            ['Password', self.secret_key],
        ]

        if 'TerminalKey' not in data:
            base.append(['TerminalKey', self.terminal_key])

        for k, v in data.items():
            if k == 'Token':
                continue
            if isinstance(v, bool):
                base.append([k, str(v).lower()])
            elif not isinstance(v, list) or not isinstance(v, dict):
                base.append([k, v])

        base.sort(key=lambda i: i[0])
        values = ''.join(map(lambda i: str(i[1]), base))

        m = hashlib.sha256()
        m.update(values.encode())
        return m.hexdigest()

    @staticmethod
    def update_payment_from_response(p: Payment, response: dict) -> Payment:
        for resp_field, model_field in Payment.RESPONSE_FIELDS.items():
            if resp_field in response:
                setattr(p, model_field, response.get(resp_field))

        return p

    def token_correct(self, token: str, data: dict) -> bool:
        return token == self._token(data)

    def init(self, p: Payment) -> Payment:
        response = self._request('INIT', requests.post, p.to_json()).json()
        return self.update_payment_from_response(p, response)

    def status(self, p: Payment) -> Payment:
        response = self._request('GET_STATE', requests.post, {'PaymentId': p.payment_id}).json()
        return self.update_payment_from_response(p, response)
