import KEYS 
import requests as r

PRICING_PATH = f"/v3/accounts/{KEYS.ACCOUNT_ID}/pricing"

PRICE_query = {"instruments": "EUR_USD"}
PRICE_headers = {
    'Content-Type': 'application/json',
    "Authorization": "Bearer "+ KEYS.TOKEN
}

PRICE_response = r.get(KEYS.API_URL+PRICING_PATH, headers=PRICE_headers, params=PRICE_query)

PRICE_data = PRICE_response.json()

if 'prices' in PRICE_data and len(PRICE_data['prices']) > 0:

    price_info = PRICE_data['prices'][0]
    
    b = price_info['bids'][0]['price']
    a = price_info['asks'][0]['price']
    
    ask = float(a)
    bid = float(b)

else:
    print("Unable to retrieve price information")
