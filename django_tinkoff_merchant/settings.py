from django.conf import settings
from django.utils.lru_cache import lru_cache

DEFAULT_CONFIG = {
    'URLS': {
        'INIT': 'https://securepay.tinkoff.ru/v2/Init',
        'GET_STATE': 'https://securepay.tinkoff.ru/v2/GetState',
        'CANCEL': 'https://securepay.tinkoff.ru/v2/Cancel',
    },
    'TAXATION': 'usn_income',
    'ITEM_TAX': 'none',
    'TERMINAL_KEY': '',
    'SECRET_KEY': '',
}


@lru_cache()
def get_config():
    user_config = getattr(settings, 'TINKOFF_PAYMENTS_CONFIG', {})

    config = DEFAULT_CONFIG.copy()
    config.update(user_config)

    return config
