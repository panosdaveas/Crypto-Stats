import json

import requests

url = 'https://rest.coinapi.io/v1/exchanges'

print(json.dumps(r, indent=4, sort_keys=True))
# print(r['confirmed'][0])
