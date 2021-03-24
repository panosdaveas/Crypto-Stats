# imports...
import requests
import pymongo
from datetime import datetime
from plot import plot_function

# create database and connect to mongoDB server
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydatabase = myclient["mydatabase"]
dblist = myclient.list_database_names()
print(dblist)
if "mydatabase" in dblist:
    print('The database exists.')

# call CoinAPI/fetch data for Bitcoin
url = 'https://rest.coinapi.io/v1/assets/BTC'
headers = {'X-CoinAPI-Key': 'B284C4BF-9B46-46F4-B377-0E1CA1EEECC7'}
response = requests.get(url, headers=headers).json()

# populate bitcoin_collection
bitcoin = mydatabase[response[0]['asset_id']]
doc = {"date": datetime.now().strftime('%d-%m-%Y, %H:%M:%S'), "price": response[0]['price_usd']}
entry = bitcoin.insert_one(doc).inserted_id

#for i in bitcoin.find({'buy': False}):
#    print(i['buy'])

# create purchase collection
purchase = mydatabase['purchase']
buy = False
last = dict

if buy is True:
    entry = purchase.insert_one(doc).inserted_id

for document in purchase.find().sort('_id', -1).limit(1):
    last = document

# Plot operations
listDates = []
listPrices = []

for document in bitcoin.find({}, {"_id": False}):
    listDates.append(document['date'])
    listPrices.append(document['price'])

plot_function(listDates, listPrices, last)

# close session
# bitcoin.drop()
#purchase.drop()
myclient.close()
