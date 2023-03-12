import os
from dotenv import load_dotenv


load_dotenv()

SAVE_DUMP = True

API_KEY = os.getenv('API_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')

dump_file = 'dump.json'
dump_tickers = ['ETHUSDT', 'ETHBTC', 'BTCUSDT']

count_base_indicator = 2500
count_short_indicator = 10