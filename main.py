import json

import requests

r = requests.get("https://covid2019-api.herokuapp.com/timeseries/confirmed").json()

print(json.dumps(r, indent=4, sort_keys=True))
# print(r['confirmed'][0])
