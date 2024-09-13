import KEYS
import candleData
import orders
import pricing

import requests
import time


class Strategy:

    def __init__(self, api_key, account_id, base_url):

        self.api_key = api_key
        self.account_id = account_id
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def _make_request(self, endpoint, params):
        URL = f"{endpoint}"
        response = requests.get(URL, headers=self.headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None

    def order(self, low_H4, curr_low, curr_close, prev_high, prev_low, M15_data):

        "Strategy Here"

        long_signal = False

        if long_signal == True:
            orders.order()
        else:
            print("No Signal")

    def get_candles_data_15(self):
        data_M15 = self._make_request(endpoint=candleData.endpoint, params=candleData.params_15)
        if data_M15 and 'candles' in data_M15:
            return data_M15['candles']

    def get_candles_data_H4(self):
        data_H4 = self._make_request(endpoint=candleData.endpoint, params=candleData.params_H4)
        if data_H4 and 'candles' in data_H4:
            return data_H4['candles']

    def get_signal(self, get_candles_data_H4, get_candles_data_15, order):
        H4_data = []
        M15_data = []

        while True:
            try:
                candles_H4 = get_candles_data_H4()
                candles_15 = get_candles_15_candle()

                for i15 in candles_15:
                    M15_data.append(i15)

                for i4 in candles_H4:
                   H4_data.append(i4)

                curr_candle = M15_data[13]
                prev_candle = M15_data[12]
                data_H4 = H4_data[2]

                curr_low = curr_candle['mid']['l']
                curr_close = curr_candle['mid']['c']
                prev_high = prev_candle['mid']['h']
                prev_low = prev_candle['mid']['l']
                low_H4 = data_H4['mid']['l']

                order(low_H4, curr_low, curr_close, prev_high, prev_low, M15_data)

                time.sleep(1)

                for i15 in candles_15:
                    M15_data.remove(i15)

                for i4 in candles_H4:
                   H4_data.remove(i4)
                
                time.sleep(1)

            except KeyboardInterrupt:
                print("Ending Session")
                break

if __name__ == "__main__":
    API_KEY = KEYS.TOKEN
    ACCOUNT_ID = KEYS.ACCOUNT_ID
    BASE_URL = KEYS.API_URL

    oanda = Strategy(api_key=API_KEY, account_id=ACCOUNT_ID, base_url=BASE_URL)

    oanda.get_signal(oanda.get_candles_data_H4, oanda.get_candles_data_15, oanda.order)
