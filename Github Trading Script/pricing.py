import KEYS 
import requests as r

PRICING_PATH = f"/v3/accounts/{KEYS.ACCOUNT_ID}/pricing"

PRICE_query = {"instruments": "EUR_USD"}
PRICE_headers = {
    'Content-Type': 'application/json',
    "Authorization": "Bearer "+ KEYS.TOKEN
}

PRICE_response = r.get(KEYS.API+PRICING_PATH, headers=PRICE_headers, params=PRICE_query)

PRICE_data = PRICE_response.json()

if 'prices' in PRICE_data and len(PRICE_data['prices']) > 0:

    price_info = PRICE_data['prices'][0]
    
    bid = price_info['bids'][0]['price']
    ask = price_info['asks'][0]['price']
    
    float_ask = float(ask)
    float_bid = float(bid)

else:
    print("Unable to retrieve price information")