# imports...
import json
import requests
import pymongo
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from pprint import pprint  # prettyPrinting

# create and connect to mangoDB
# pip3 install mongodb-community@4.4
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydatabase = myclient["mydatabase"]
dblist = myclient.list_database_names()
print(dblist)
if "mydatabase" in dblist:
    print('The database exists.')
# call CoinAPI/v1 for Bitcoin
url = 'https://rest.coinapi.io/v1/assets/BTC'
headers = {'X-CoinAPI-Key': 'B284C4BF-9B46-46F4-B377-0E1CA1EEECC7'}
response = requests.get(url, headers=headers).json()
# write to file --optional
output = open("output.json", "w")
output.write(json.dumps(response, indent=4))  # write to file
# populate bitcoin_database
bitcoin = mydatabase[response[0]['asset_id']]
doc = {"date": datetime.now().strftime('%d-%m-%Y-%H-%M-%S'), "price": response[0]['price_usd']}
x = bitcoin.insert_one(doc).inserted_id

listDates = []
listPrices = []

for document in bitcoin.find({}, {"_id": False}):
    listDates.append(document['date'])
    listPrices.append(document['price'])

# Plot operations
# pip3 install matplotlib
xpoints = np.array(listDates)
ypoints = np.array(listPrices)
plt.plot(ypoints)
plt.show()
# close session
#bitcoin.drop()
myclient.close()
