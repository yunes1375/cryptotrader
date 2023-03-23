import os
from dotenv import load_dotenv
load_dotenv()
MEXC_API_KEY = os.getenv('MEXC_API_KEY')
MEXC_API_SECRET = os.getenv('MEXC_API_SECRET')
MEXC_SIGNATURE = os.getenv('MEXC_SIGNATURE')
MEXC_API_URL = os.getenv('MEXC_API_URL')