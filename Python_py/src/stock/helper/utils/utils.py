import json
import os
import sys
import json
import datetime as dt
from pathlib import Path
class utils:
    def __init__(self):
        pass

    @staticmethod
    def file_read():
        try:
            file = open('stock.txt', 'open mode')
        except EOFError as ex:
            print("Caught the EOF error.", ex )
            raise ex
        except IOError as e:
            print("Caught the I/O error.", e)
            raise ex    

    @staticmethod
    def load_all_tickers(path):
        base_path = Path(__file__).parent
        file_path = (base_path / "../../../../data/stock_list.txt").resolve()
        stocks = open(file_path, "r").readlines()
        stocks = [str(item).strip("\n") for item in stocks]
        stocks = list(sorted(set(stocks)))
        return stocks

    @staticmethod
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


    @staticmethod
    def get_configFile(setup):
        if setup == 'apikey':
            with open("//user//config.json", "r") as jsonfile:
                data = json.load(jsonfile) # Reading the file
            print("Read successful")
            jsonfile.close()
        # elif setup is 'folderpath':
        #     pass
        # elif setup is 'user':
        #     pass
        # else:
        #     print('do nothing')