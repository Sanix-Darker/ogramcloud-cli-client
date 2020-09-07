# OgramCloud-CLI-client

This is CLI interface for the free UNLIMITED STORAGE of [OgramCloud](https://ogramcloud.com)/[Source-code](https://github.com/Sanix-Darker/ogramcloud) service.

## Production-Setup

### Download the latest release

You just have to og on [Releases](https://github.com/Sanix-Darker/ogramcloud-cli-client/releases) and get the version you want for your system.

### How to use it

- To upload a file, just hit :
```shell
occ -f ./your/file.path
```

- To get the file with the file-key, just hit :
```shell
occ -i iooooiiiiiooooo
```

- To get help :
```shell
occ -h

usage: occ [-h] [-f FILEPATH] [-i ID] [-c CHATID] [-u HOSTURL]

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

## Development-Setup

### How to install

- After cloning the project :
```shell
git clone https://github.com/Sanix-Darker/ogramcloud-cli-client
```

- After creating your Virtualenv :
```shell
pip install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
```

- Copy the `example.config.txt` to `config.txt` and provide corrects informations

- Install dependencies:
```shell
pip install -r requirements.txt
```

### How to launch

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

- To build the executable :
```shell
# You install pyinstaller
pip3 install pyinstaller

# To build the executable using pyinstaller
pyinstaller main.py --name occ \
 --hiddenimport=requests \
 --hiddenimport=configparser \
 --exclude-module=pytest \
 --onefile
```

## Author

- Sanix-darker

## LICENSE

[MIT - LICENSE](https://github.com/Sanix-Darker/ogramcloud-cli-client/blob/master/LICENSE)
