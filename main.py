# imports...
import pymongo
from plot import plot_function
from Math import price_calculator

# create database and connect to mongoDB server
myclient = pymongo.MongoClient('mongodb://localhost:27017')
mydatabase = myclient['mydatabase']
dblist = myclient.list_database_names()
print(dblist)
if 'mydatabase' in dblist:
    print('The database exists.')
bitcoin = mydatabase['BTC']


# queries
last_entry = list(bitcoin.find().sort('_id', -1).limit(1))
last_open_trade = list(bitcoin.find({'buy': {'$exists': 1}}).sort('date', -1).limit(1))
results = list(bitcoin.find({}, {'_id': False}))


# buy
open_trade = False
if open_trade:
    bitcoin.update_one(last_entry[0], {'$set': {'buy': True}})


# close trades
def close_trades():
    for trade in bitcoin.find({'buy': True}):
        bitcoin.update_one({'_id': trade['_id']}, {'$set': {'buy': False}})
        print(trade['_id'])


# math operations
current_trade = price_calculator(results, last_open_trade)

# plot operations
plot_function(results, current_trade)

# close session
#myclient.close()
