# utils functions for ogram-cli-client
import requests
import json
from os import path
from sys import exit


def upload(file_path: str, host_url: str, chat_id: str):
    """
    This method will proceed the upload to Ogram-API
    ::file_path:: The file path of the file you want to upload
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

    print("[+] Fetching file info...")

    r = requests.get(host_url + "/api/checkfile/" + oid)
    info = json.loads(r.content.decode())

    if info["status"] == "success":
        print("[+] Getting file " + info["file_name"] + "...")
        print("[+] Chunks : " + str(info["chunks"]))

        print("[+] Downloading your file...")

        r2 = requests.get(host_url + "/api/file/" + oid)

        with open(info["file_name"], "wb") as fr:
            fr.write(r2.content)
            print("[+] file downloaded successfully !")
    else:
        print("[x] Error, your ogram-file-key is not valid !")


def install():
    
    print("[-] Installation of your OgramCloud-CLI-client")
    if path.exists("config.txt"):
        print("[-] A configuration file have been detected, do you want to procedd installation anyway !?")
        choice = input("choice (y/n):")
        if choice.lower() == "n":
            print("[-] Stopping installation !")
            exit()
        else:
            print("[+] Proceeding the installation..")

    