import configparser
import os


class Config:
    __config = configparser.ConfigParser()

    def __init__(self):
        self.__config.read(os.path.expanduser("~/.giticonf"))

    def get_proxy(self):
        if 'proxy' in self.__config:
            if 'address' in self.__config['proxy']:
                return self.__config['proxy']['address']

    def set_proxy(self, url):
        self.__config['proxy']['address'] = url
