import json

import requests

import pymongo

from pymongo import MongoClient
#myclient = MongoClient() #connect to default host & port
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["mydatabase"]

dblist = myclient.list_database_names()
print(dblist)

if "mydatabase" in dblist:
    print('The database exists.')

url = 'https://rest.coinapi.io/v1/exchanges'
headers = {'X-CoinAPI-Key': 'B284C4BF-9B46-46F4-B377-0E1CA1EEECC7'}
response = requests.get(url, headers=headers).json()


mycol = mydb["cryptos"]
x = mycol.insert_many(response)

print(mydb.list_collection_names())
query = mycol.find({"exchange_id": {"$regex": "^B"}})
for y in query:
    print(y)
#mycol.drop()

#with open('output.json', 'w') as outfile:
#    json.dump(response, outfile)
#
