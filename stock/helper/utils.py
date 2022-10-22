import json
import os
import sys
import json
import datetime as dt
from pathlib import Path

def file_read():
    try:
        file = open('stock.txt', 'open mode')
    except EOFError as ex:
        print("Caught the EOF error.", ex )
        raise ex
    except IOError as e:
        print("Caught the I/O error.", e)
        raise ex    


def load_user_tickers(username):
    try:
        base_path = Path(__file__).parent
        base_path = os.path.join(base_path / "../../../../config/user/", username + ".json")
        with open(base_path, "r") as jsonfile:
            data = json.load(jsonfile)
        jsonfile.close()
        print("Reading json file for user {} was successful.")
        return data
    except EOFError as ex:
        print("Caught the EOF error.", ex )
        raise ex
    except IOError as e:
        print("Caught the I/O error.", e)
        raise ex    


def get_config_file(setup):
    base_path = Path(__file__).parent.parent
    base_path = os.path.join(base_path / "../config/", setup + ".json")
    if setup == 'apikey':
        with open(base_path, "r") as jsonfile:
            data = json.load(jsonfile)
    elif setup == "user_settings":
        with open(base_path, "r") as jsonfile:
            data = json.load(jsonfile)
    elif setup == "folderpath":
        with open(base_path, "r") as jsonfile:
            data = json.load(jsonfile)
    else:
        with open(base_path, "r") as jsonfile:
            data = json.load(jsonfile)


    jsonfile.close()
    return data
