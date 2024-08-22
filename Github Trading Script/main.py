import yfinance as yf
from collections import deque
import time
import requests as r
import json as j

import orders

def main():
    ticker = "EURUSD=X"
    interval = "1h"
    interval_daily = "1d"
    period = "10d"

    while True:
        try:
            priceData = yf.download(tickers=ticker, interval=interval, period=period)
            priceDataDaily = yf.download(tickers=ticker, interval=interval_daily, period=period)

            daily_high = deque(priceDataDaily['High'].tail(3), maxlen=5)
            prices_close = deque(priceData['Close'].tail(3), maxlen=100)
            prices_high = deque(priceData['High'].tail(3), maxlen=5)
            prices_open = deque(priceData['Open'].tail(3), maxlen=5)

            get_signals(daily_high,prices_close,prices_high,prices_open,priceData)

            time.sleep(3601)

        except KeyboardInterrupt:
            print("Ending trading session")
            break


def get_signals(daily_high,prices_close,prices_high,prices_open,priceData):

    " *********** strategy here ***********"

    short_signal = True

    if short_signal == True:
        orders.order()
    else:
        print("No Short")


if __name__ == "__main__":
    main()