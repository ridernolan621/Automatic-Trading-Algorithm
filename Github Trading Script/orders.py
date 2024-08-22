import requests as r
import json as j

import KEYS
import pricing

def order():

    ORDERS_PATH = f"/v3/accounts/{KEYS.ACCOUNT_ID}/orders"

    ORDER_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {KEYS.TOKEN}"
    }

    order_data = {
        "order": {
            "units": "-10",
            "instrument": "EUR_USD",
            "timeInForce": "GTC",  
            "type": "LIMIT",
            "price": pricing.bid
        }
    }

    stop_data = {
        "order": {
            "symbol": "EURUSD", 
            "side": "SELL", 
            "type": "TRAILING_STOP_LOSS",
            "clientTradeID": "my_trade_123",
            "price": pricing.bid,
            "timeInForce": "GTC",
            "quantity": "-10",
            "trailingStopValue": 20
        }
    }

    ORDER_response = r.post(KEYS.API+ORDERS_PATH,
            headers=ORDER_headers,
            data=j.dumps(order_data)
        )

    STOP_ORDER_response = r.post(KEYS.API+ORDERS_PATH,
            headers=ORDER_headers,
            data=j.dumps(stop_data))

    if ORDER_response.status_code == 201:
        order_response_data = ORDER_response.json()
    
        trade_id = order_response_data['orderFillTransaction']['id']

        stop_data = {
            "order": {
                "type": "TRAILING_STOP_LOSS",
                "tradeID": trade_id,
                "distance": "0.0025",
                "timeInForce": "GTC",
                "triggerCondition": "DEFAULT"
            }
        }

        STOP_ORDER_response = r.post(KEYS.API+ORDERS_PATH,
            headers=ORDER_headers,
            data=j.dumps(stop_data))
        
        if STOP_ORDER_response.status_code == 201:
            print("Stop Order Created")
            print(stop_data)
        else:
            print("Stop Order Failed:", STOP_ORDER_response.json())

    else:
        print("Main order failed:", ORDER_response.json())


if __name__ == "__main__":
    order()