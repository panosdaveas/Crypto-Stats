# imports...
import json
import requests
import pymongo

# create and connect to mangoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydatabase = myclient["mydatabase"]
dblist = myclient.list_database_names()
print(dblist)
if "mydatabase" in dblist:
    print('The database exists.')
# call CoinAPI/v1
url = 'https://rest.coinapi.io/v1/assets'
headers = {'X-CoinAPI-Key': 'B284C4BF-9B46-46F4-B377-0E1CA1EEECC7'}
response = requests.get(url, headers=headers).json()
# write to file --optional
# output = open("output.json", "w")
# output.write(json.dumps(response, indent=4)) # write to file
# print(json.dumps(response, indent=4)) # printAll

# populate database's collection
mycollection = mydatabase["cryptos"]
for key in response:
    if 'price_usd' in key:
        mydict = {'asset_id': key['asset_id'], 'price_usd': key['price_usd']}
        x = mycollection.insert_one(mydict).inserted_id

listid = mycollection.distinct("asset_id")
listprice = mycollection.distinct("price_usd")
for i in range(len(listid)):
    print(listid[i], listprice[i])

# close session
mycollection.drop()
myclient.close()
