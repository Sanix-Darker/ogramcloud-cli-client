# Settings.py for ogramcloud-cli-client
# First, install configparser using "pip install configparser"
import configparser
from app.utils import install_config
from os import path

if not path.exists("config.txt"):
    install_config()

# Configs parameters
conf = configparser.RawConfigParser()
configFilePath = r'config.txt'
conf.read(configFilePath)

# Filling parameters

# The version of this project
__version__ = '0.0.1'
# your personnal chat_id
CHAT_ID = conf.get('oclients-config', 'CHAT_ID')

# the Host url, as default it will take OgramCloud.com
HOST_URL = conf.get('oclients-config', 'HOST_URL')
