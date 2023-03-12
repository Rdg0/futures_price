import time

from collections import deque
from binance.spot import Spot


from correlation import get_correlation_coefficient
from dump import create_dump
from settings import (
    API_KEY, SECRET_KEY, dump_tickers, dump_file, SAVE_DUMP,
    count_base_indicator, count_short_indicator
)

client = Spot(API_KEY, SECRET_KEY)

deque_ethusdt_short = deque(maxlen=count_short_indicator)
deque_btcusdt_short = deque(maxlen=count_short_indicator)

deque_ethusdt_base = deque(maxlen=count_base_indicator)
deque_btcusdt_base = deque(maxlen=count_base_indicator)


counter = 0



while True:
    
    try:
        tickers = client.ticker_price(symbols=dump_tickers)
    except Exception as error:
        print(f'При получении данных от Binance произошла ошибка: {error}')
        time.sleep(1)
        continue
    if SAVE_DUMP:
        create_dump(tickers)

    if counter >= count_short_indicator:
        deque_btcusdt_short.popleft()
        deque_ethusdt_short.popleft()
    if counter >= count_base_indicator:
        deque_btcusdt_base.popleft()
        deque_ethusdt_base.popleft()

    for ticker in tickers:
        if ticker['symbol'] == 'BTCUSDT':
            deque_btcusdt_base.append(float(ticker['price']))
            deque_btcusdt_short.append(float(ticker['price']))
        elif ticker['symbol'] == 'ETHUSDT':
            deque_ethusdt_base.append(float(ticker['price']))
            deque_ethusdt_short.append(float(ticker['price']))
    counter += 1
    if counter > count_short_indicator:
        corr_base = get_correlation_coefficient(deque_btcusdt_base, deque_ethusdt_base)
        corr_short = get_correlation_coefficient(deque_btcusdt_short, deque_ethusdt_short)

        if corr_base > corr_short:
            price_eth_delta = (deque_ethusdt_short[-1] - deque_ethusdt_short[0])/(deque_ethusdt_short[0] / 100)
            if price_eth_delta >= 1:
                print('Отклонение собственной цены составило 1% или более.')
        
    time.sleep(1)



if __name__ == "__main__":
    main()
