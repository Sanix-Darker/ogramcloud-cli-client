# Settings.py for ogramcloud-cli-client
# First, install configparser using "pip install configparser"
import configparser

# Configs parameters
conf = configparser.RawConfigParser()   
configFilePath = r'config.txt'
conf.read(configFilePath)

# Filling parameters
CHAT_ID = conf.get('oclients-config', 'CHAT_ID')
HOST_URL = conf.get('oclients-config', 'HOST_URL')
