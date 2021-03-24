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
buy = False
doc = {"date": datetime.now().strftime('%d-%m-%Y, %H:%M:%S'), "price": response[0]['price_usd']}
if buy:
    doc['buy'] = True  # append dict when a purchase takes place
entry = bitcoin.insert_one(doc).inserted_id
#bitcoin.update_many({'buy': {'$exists': 1}}, {'$unset': {'buy': 1}})  # delete field: 'buy'

# Plot operations
purchases = list(bitcoin.find({'buy': {'$exists': 1}}).sort('date', -1).limit(1))
results = list(bitcoin.find({}, {"_id": False}))
plot_function(results, purchases)

# close session
# bitcoin.drop()
myclient.close()
