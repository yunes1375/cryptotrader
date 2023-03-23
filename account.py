import time
from settings import MEXC_API_KEY, MEXC_API_SECRET, MEXC_SIGNATURE, MEXC_API_URL
import requests
import hmac
import hashlib


# Endpoints use HMAC SHA256 signatures. The HMAC SHA256 signature is a keyed HMAC SHA256 operation. Use your secretKey as the key and totalParams as the value for the HMAC operation
def signature_maker(**kwargs):

    secret_key = MEXC_API_SECRET
    total_params = "&".join(f"{key}={value}" for key, value in kwargs.items())
    signature = hmac.new(secret_key.encode('utf-8'), total_params.encode('utf-8'), hashlib.sha256).hexdigest()
    kwargs['signature']=signature
    return kwargs

def account_data():

    url = MEXC_API_URL + 'account'

    headers = {"Content-Type": "application/json; charset=utf-8", 'x-mexc-apikey': MEXC_API_KEY,
               'api_secret': MEXC_API_SECRET}
    
    initial_params={
        "timestamp": int(time.time() * 1000)
        }
    params=signature_maker(**initial_params)

    response = requests.get(url, params=params, headers=headers)
    
account_data()