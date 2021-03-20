import json

import requests

url = 'https://rest.coinapi.io/v1/exchanges'
headers = {'X-CoinAPI-Key' : 'B284C4BF-9B46-46F4-B377-0E1CA1EEECC7'}
r = requests.get(url, headers=headers).json()

print(json.dumps(r, indent=4, sort_keys=True))
# print(r['confirmed'][0])
