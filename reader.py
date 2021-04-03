# imports...
import pymongo

from player import alert_open, alert_close, percent_diff
from plot import plot_function
from config import Config


def read():
    config = Config()
    # create database and connect to mongoDB server
    myclient = pymongo.MongoClient(config.get_db_url())
    mydatabase = myclient[config.get_db_name()]
    bitcoin = mydatabase[config.get_api_asset()]
    dblist = myclient.list_database_names()
    print(dblist)
    if config.get_db_name() in dblist:
        print('The database exists.')

    # queries
    results = list(bitcoin.find({}, {'_id': False}))
    last_entry = list(bitcoin.find().sort('_id', -1).limit(1))
    last_trade = list(bitcoin.find({'buy': {'$exists': 1}}).sort('date', -1).limit(1))
    last_open_trade = list(bitcoin.find({'buy': True}).sort('date', -1).limit(1))

    # open/close trades
    open_trade = alert_open(results, last_trade)
    if open_trade:
        bitcoin.update_one(last_entry[0], {'$set': {'buy': True}})
        print('buy')

    close_trade = alert_close(results, last_trade)
    if close_trade:
        bitcoin.update_one(last_entry[0], {'$set': {'buy': False}})
        bitcoin.update_one(last_open_trade[0], {'$set': {'sold': dict(
            price_sold=last_entry[0]['price'], date_sold=last_entry[0]['date'],
            profit=percent_diff(last_entry[0]['price'], last_open_trade[0]['price']))}})
        print('sell')

    # plot operations
    plot_function(results, last_open_trade)


if __name__ == '__main__':
    read()
