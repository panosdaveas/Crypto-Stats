"""
This file defines how the configuration is red

A sample config is the following:

[DATABASE]
type = mongodb
ip = 192.168.1.5
port = 27017
name = mydatabase

[API]
url = https://rest.coinapi.io/v1/assets/
asset = BTC
key = B284C4BF-9B46-46F4-B377-0E1CA1EEECC7
"""

import configparser

"""
Config class
"""


class Config:
    def __init__(self, config_file='config'):
        """
        init config
        """

        config = configparser.ConfigParser()
        config.read(config_file)
        self.db_config = config['DATABASE']
        self.api_config = config['API']

    def get_db_url(self):
        """
        Return db url in the form <db_type>://<ip>:<port>
        """
        return self.db_config['type'] + '://' + self.db_config['ip'] + ':' + self.db_config['port']

    def get_db_name(self):
        """
        Return db name 
        """
        return self.db_config['name']

    def get_api_url(self):
        """
        Return api url in the form <url><asset>
        Assets can be BTC, ETH, etc
        """
        return self.api_config['url'] + self.api_config['asset']

    def get_api_asset(self):
        """
        Return api assets
        TODO: support more assets later
        """
        return self.api_config['asset']

    def get_api_key(self):
        """
        Return api key
        """
        return self.api_config['key']


def main():
    config = Config()
    print("DB URL:", config.get_db_url())
    print("DB name:", config.get_db_name())
    print("API URL:", config.get_api_url())
    print("API asset:", config.get_api_asset())
    print("API key:", config.get_api_key())


if __name__ == "__main__":
    main()
