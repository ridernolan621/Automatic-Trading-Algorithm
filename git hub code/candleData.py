import KEYS

EURO = "EUR_USD"

path = f"/v3/instruments/{EURO}/candles"
endpoint = (KEYS.API_URL+path)

params_H4 = {
    "count": 5,
    "granularity": "H4",
    "price": "M"
}

params_15 = {
    "count": 15,
    "granularity": "M15",
    "price": "M"
}