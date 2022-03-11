
import configparser
import os, json
from configparser import ConfigParser



os.chdir('./INIFiles')

config = ConfigParser()
config.read('config.ini')
print(config['database_connections'].get('username'),
      config['database_connections'].get('password') )