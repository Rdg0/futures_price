import datetime as dt
import json
from settings import dump_file

def create_dump(tickers):
    """Создание дампа данных."""
    prices = {}
    time_now = dt.datetime.now().strftime('%H:%M:%S %m.%d.%Y')
    with open(dump_file, 'a') as f:
        for ticker in tickers:
            if time_now not in prices:
                prices[time_now] = dict([(ticker['symbol'], float(ticker['price']))])
            else:
                prices[time_now][ticker['symbol']]=float(ticker['price'])
        frame = {time_now: prices.get(time_now)}
        json.dump(frame, f)
        f.write('\n')

def convert():
    filename = 'dump.json'
    convert_to_file = 'true.json'
    dump_dict = {}
    with open(filename) as f:
        for line in f:
            frame = json.loads(line)
            dump_dict.update(frame)


    with open(convert_to_file, 'w') as f:
        json.dump(dump_dict, f)

