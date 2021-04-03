# imports...
from datetime import datetime

import pymongo
import requests
from config import Config


def write():
    config = Config()
    # create database and connect to mongoDB server
    myclient = pymongo.MongoClient(config.get_db_url())
    mydatabase = myclient[config.get_db_name()]
    dblist = myclient.list_database_names()

    # call CoinAPI/fetch data for Bitcoin
    url = config.get_api_url()
    headers = {'X-CoinAPI-Key': config.get_api_key()}
    response = requests.get(url, headers=headers).json()

    # populate bitcoin_collection
    bitcoin = mydatabase[response[0]['asset_id']]
    doc = {'date': datetime.now().strftime('%d-%m-%Y, %H:%M:%S'),
           'price': response[0]['price_usd']}
    entry = bitcoin.insert_one(doc).inserted_id

    # queries for log
    query = list(bitcoin.find().sort('_id', -1).limit(1))
    print(query)

    # close session
    # bitcoin.drop()
    myclient.close()


if __name__ == '__main__':
    write()
