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
    def path_test():
        print('This is static method!')

    def path_testing(self):
        print("haha")

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
    def load_ticker(path):
        base_path = Path(__file__).parent
        file_path = (base_path / "../../../../data/stock_list.txt").resolve()
        stocks = open(file_path, "r").readlines()
        stocks = [str(item).strip("\n") for item in stocks]
        stocks = list(sorted(set(stocks)))
        return stocks

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