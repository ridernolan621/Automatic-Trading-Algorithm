import requests as r
import json as j
import time as t

import KEYS
import pricing
import trader


def order():

    ORDERS_PATH = f"/v3/accounts/{KEYS.ACCOUNT_ID}/orders"

    ORDER_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {KEYS.TOKEN}"
    }

    order_data = {
        "order": {
            "units": "10",
            "instrument": "EUR_USD",
            "timeInForce": "GTC",  
            "type": "LIMIT",
            "price": pricing.b
        }
    }

    ORDER_response = r.post(KEYS.API_URL+ORDERS_PATH,
            headers=ORDER_headers,
            data=j.dumps(order_data)
        )

    if ORDER_response.status_code == 201:
        order_response_data = ORDER_response.json()
        trade_id = order_response_data['orderCreateTransaction']['id']

        print("Order Placed")

        # wait 5 minutes for order to be filled
        t.sleep(300)

        stop_data = {
            "order": {
                "type": "TRAILING_STOP_LOSS",
                "tradeID": trade_id,
                "distance": "-0.0010",
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


#def orderFill():
#
#    ORDER_PENDING_path = f"/v3/accounts/{KEYS.ACCOUNT_ID}/pendingOrders/"
#
#    ORDER_PENDING_headers = {
#        "Content-Type": "application/json",
#        "Authorization": f"Bearer {KEYS.TOKEN}"
#    }
#
#    ORDER_PENDING_response = r.get(KEYS.API+ORDER_PENDING_path, ORDER_PENDING_headers)
#
#    if ORDER_PENDING_response.status_code == 200:
#        order_data = ORDER_PENDING_response.json()
#        print(order_data)
#    else:
#        print("Error", ORDER_PENDING_response.status_code)
#        order_data = ORDER_PENDING_response.json()
#        print(order_data)


if __name__ == "__main__":
    order()