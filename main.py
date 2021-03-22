# imports...
import json
import requests
import pymongo
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# create database and connect to mangoDB server
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

# populate bitcoin_database
bitcoin = mydatabase[response[0]['asset_id']]
doc = {"date": datetime.now().strftime('%d-%m-%Y, %H:%M:%S'), "price": response[0]['price_usd']}
x = bitcoin.insert_one(doc).inserted_id

# Plot operations
listDates = []
listPrices = []

for document in bitcoin.find({}, {"_id": False}):
    #formatted_date = document['date'].split(",")
    listDates.append(document['date'])
    listPrices.append(document['price'])

xpoints = np.array(listDates)
ypoints = np.array(listPrices)
plt.plot(ypoints, linewidth=0.6)
plt.grid(axis='y', linestyle='dotted', linewidth=0.5)
plt.axhline(y=57500, color='r', linestyle='--', linewidth=0.5)
plt.show()

# close session
#bitcoin.drop()
myclient.close()
