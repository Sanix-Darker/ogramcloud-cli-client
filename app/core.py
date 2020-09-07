# main client
import argparse
from app.settings import CHAT_ID, HOST_URL
from app.utils import upload, getFile

__version__ = '0.0.1'

def main():
    # Initialize the arguments
    # Example command :
    # To upload : python3 -m app.main -f ./your/file.path
    # To get your file : python3 -m app.main -i 0101010101010
    prs = argparse.ArgumentParser()
    prs.add_argument('-f', '--filepath', 
                        help='File path of the file we want to upload', type=str)
    prs.add_argument('-i', '--id', 
                        help='OgramCloud Id for regenerating our file', type=str)
    prs.add_argument('-c', '--chatid', 
                        help='Chat Id on Telegram account, see documentation of (https://ogramcloud.com)', 
                        type=str, required=False, default=CHAT_ID)
    prs.add_argument('-u', '--hosturl', 
                        help='The host url of OgramCloud', 
                        type=str, required=False, default=HOST_URL)
    prs.add_argument('-v', '--version', action='version', 
                        help='The version of the OgramCloud-CLI-client',
                        version='OgramCloud-CLI-client v' + __version__)
    prs = prs.parse_args()

    if prs.filepath != None:
        upload(prs.filepath, prs.hosturl, prs.chatid)
    else:
        if prs.id != None:
            getFile(prs.id, prs.hosturl)
        else:
            print("[x] Error : Please make sur to provie rights parameters !")