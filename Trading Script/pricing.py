import KEYS 
import requests as r

path = f"/v3/accounts/{KEYS.ACCOUNT_ID}/pricing"
endpoint = (KEYS.API_URL+path)

params = {"instruments": "EUR_USD"}

headers = {
    'Content-Type': 'application/json',
    "Authorization": "Bearer "+ KEYS.TOKEN
}