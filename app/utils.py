# utils functions for ogram-cli-client
import requests
import json
from os import path
from sys import exit


def upload(file_path: str, host_url: str, chat_id: str):
    """
    This method will proceed the upload to Ogram-API

    ::file_path:: The file path of the file you want to upload
    ::host_url:: The Host of the server where Ogram is running, as default ogramcloud.com
    ::chat_id:: Your chat-id
    """
    
    files = {
        "file": open(file_path, "rb")
    }
    values = {
        "chat_id": chat_id
    }

    r = requests.post(
        host_url + "/api/upload", 
        files=files, 
        data=values
    )

    content = r.content.decode()

    print(host_url + "/api/file/" + json.loads(content)["file_key"])


def getFile(oid: str, host_url: str):
    """
    This method will get file from the ogramCloud-Id

    ::oid:: The OgramCloudId of your file or the file-key
    ::host_url:: The Host of the server where Ogram is running, as default ogramcloud.com
    """
    print("[+] Fetching file info...")

    r = requests.get(host_url + "/api/checkfile/" + oid)
    info = json.loads(r.content.decode())

    if info["status"] == "success":
        print("[+] Getting file " + info["file_name"] + "...")
        print("[+] Chunks : " + str(info["chunks"]))

        print("[+] Downloading your file...")
        
        # ping
        r2 = requests.get(host_url + "/api/file/" + oid)
        if r2.status_code == 200:
            print("[+] ping... ")
            # pong
            r3 = requests.get(host_url + "/api/file/" + oid)

            if r3.status_code == 200:
                print("[+] pong....")
                with open(info["file_name"], "wb") as fr:
                    fr.write(r3.content)
                    print("[+] file downloaded successfully !")
            else:
                print("[x] Failed to pong, please retry...")
        else:
            print("[x] Failed to ping, please retry...")
    else:
        print("[x] Error, your ogram-file-key is not valid !")


def install_config():
    """
    This method will just set the configuration file and then run using parrameters in it
    """
    print("[-] Installation of your OgramCloud-CLI-client")
    if path.exists("config.txt"):
        print("[-] A configuration file have been detected, do you want to procedd installation anyway !?")
        choice = input("choice (y/n):")
        if choice.lower() == "n":
            print("[-] Stopping installation !")
            exit()
        else:
            print("[+] Proceeding the installation..")

    print("\n[-] To use OgramCloud-CLI-client, you need to set a config.txt file where your chat-id will be store !")
    chat_id = input("[+]> chat-id* (Get it with the ogram-bot (https://t.me/omega_gram_bot)) :")
    
    while len(chat_id) <= 2:
        print("[x] Error, You need to provide a valid Chat-Id tomake Occ work !")
        chat_id = input("[+]> chat-id* (Get it with the ogram-bot (https://t.me/omega_gram_bot)) :")
    
    host_url = input("[+]> host-url (Leave it blank if you don't have your own Server, https://ogramcloud.com as default):")
    default_host = "https://ogramcloud.com"

    if len(host_url) <= 1:
        host_url = default_host

    to_write = """[oclients-config]
CHAT_ID=""" + chat_id + """
HOST_URL=""" + host_url + """
"""
    with open("config.txt", "w") as frr:
        frr.write(to_write)

    print("[+] Configuration setted successfully, you can now run OCC at any time !")
    exit()
