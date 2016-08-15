import configparser
import os


class Config:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(os.path.expanduser("~/.giticonf"))
