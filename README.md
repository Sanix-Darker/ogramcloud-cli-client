# OgramCloud-CLI-client

This is just an implementation of a python client for (OgramCloud)[https://ogramcloud.com]

## How to install

- After creating your Virtualenv :
```shell
pip install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
```

- Install dependencies:
```shell
pip install -r requirements.txt
```

## How to launch

- To upload a file, just hit :
```shell
python3 -m app.main -f ./your/file.path
```

- To get the file with the file-key, just hit :
```shell
python3 -m app.main -i iooooiiiiiooooo
```

- To get help :
```shell
python3 -m app.main -h

usage: main.py [-h] [-f FILEPATH] [-i ID] [-c CHATID] [-u HOSTURL]

optional arguments:
  -h, --help            show this help message and exit
  -f FILEPATH, --filepath FILEPATH
                        File path of the file we want to upload
  -i ID, --id ID        OgramCloud Id for regenerating our file
  -c CHATID, --chatid CHATID
                        Chat Id on Telegram account, see documentation of
                        (https://ogramcloud.com)
  -u HOSTURL, --hosturl HOSTURL
                        The host url of OgramCloud
```

## Author

- sanix-darker
