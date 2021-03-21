# imports...
import json
import requests
import pymongo
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint

# create and connect to mangoDB
# pip3 install mongodb-community@4.4
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
# currently with asset's name & price in usd
mycollection = mydatabase["cryptos"]
myCryptos = {"BTC", "ETH", "DOGE", "ADA", "BNB"}
for key in response:
    if 'price_usd' in key:
        mydict = {"asset_id": key['asset_id'], "price_usd": key['price_usd']}
        x = mycollection.insert_one(mydict).inserted_id

listName = [mycollection.count_documents({})]
listPrice = [mycollection.count_documents({})]
for i in mycollection.find():
    print('{0} {1}'.format(i['asset_id'], i['price_usd']))
    listName.append(i['asset_id'])
    listPrice.append(i['price_usd'])

query1 = mycollection.find_one({"asset_id": "BTC"})
query2 = mycollection.find_one({"asset_id": "ETH"})
for i in mycollection.find():
    print(i)
# Plot operations
# pip3 install matplotlib
xpoints = np.array(listName[0:10])
ypoints = np.array(listPrice[0:10])
plt.scatter(xpoints, ypoints)
plt.show()

# close session
#mycollection.drop()
#myclient.close()
