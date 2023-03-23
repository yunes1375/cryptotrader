import time
from settings import MEXC_API_KEY, MEXC_API_SECRET, MEXC_SIGNATURE, MEXC_API_URL
import requests


def account_data():
    url = MEXC_API_URL + 'account'
    headers = {"Content-Type": "application/json; charset=utf-8", 'x-mexc-apikey': MEXC_API_KEY,
               'api_secret': MEXC_API_SECRET}
    params = {
        "timestamp": int(time.time() * 1000),
        "signature": MEXC_SIGNATURE
    }

    response = requests.get(url, params=params, headers=headers)
    print(response)
