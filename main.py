import json
import requests
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydatabase = myclient["mydatabase"]
dblist = myclient.list_database_names()
print(dblist)
if "mydatabase" in dblist:
    print('The database exists.')

url = 'https://rest.coinapi.io/v1/exchanges'
headers = {'X-CoinAPI-Key': 'B284C4BF-9B46-46F4-B377-0E1CA1EEECC7'}
response = requests.get(url, headers=headers).json()

#print(json.dumps(response, indent=4))

mycollection = mydatabase["cryptos"]
x = mycollection.insert_many(response)
myclient.close()

print(mydatabase.list_collection_names())
for i in range(len(response)):
    print(response[i]['exchange_id'], response[i]['volume_1hrs_usd'])

# query = mycollection.find({"exchange_id": {"$regex": "^BTC"}})
# mycollection.drop()
