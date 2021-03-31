# imports...
import pymongo

from Math import price_calculator, alert
from plot import plot_function

# create database and connect to mongoDB server
myclient = pymongo.MongoClient('mongodb://localhost:27017')
mydatabase = myclient['mydatabase']
dblist = myclient.list_database_names()
#print(dblist)
#if 'mydatabase' in dblist:
#    print('The database exists.')
bitcoin = mydatabase['BTC']

# queries
results = list(bitcoin.find({}, {'_id': False}))
last_entry = list(bitcoin.find().sort('_id', -1).limit(1))
trades = list(bitcoin.find({'buy': {'$exists': 1}}).sort('date', -1))
last_trade = list(bitcoin.find({'buy': {'$exists': 1}}).sort('date', -1).limit(1))
last_open_trade = list(bitcoin.find({'buy': True}).sort('date', -1).limit(1))

# math operations
current_trade = price_calculator(results, last_open_trade)

# open trade
#open_trade = False
open_trade = alert(results, last_trade)
if open_trade is not None:
    if open_trade:
        bitcoin.update_one(last_entry[0], {'$set': {'buy': True}})
    else:
        bitcoin.update_one(last_entry[0], {'$set': {'buy': False}})
        bitcoin.update_one(last_open_trade[0], {'$set': {'sold': dict(
            price_sold=last_entry[0]['price'], date_sold=last_entry[0]['date'])}})


# close trades
def close_trades():
    for trade in bitcoin.find({'buy': True}):
        bitcoin.update_one({'_id': trade['_id']}, {'$set': {'buy': False}})


# plot operations
#plot_function(results, current_trade)
