import json
import os
import sys
import json
import csv
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
    def load_all_tickers():
        matchers = ['#', '/']
        base_path = Path(__file__).parent
        file_path = (base_path / "../../../../data/stock_list.txt").resolve()
        stocks = open(file_path, "r").readlines()
        stocks = [str(item).strip("\n") for item in stocks]
        element = [x for x in stocks if "#" not in x]
        return list(sorted(set(element)))

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
        base_path = Path(__file__).parent
        base_path = os.path.join(base_path / "../../../../config/", setup + ".json")
        if setup == 'apikey':
            with open(base_path, "r") as jsonfile:
                data = json.load(jsonfile)
        elif setup == "user_settings":
            with open(base_path, "r") as jsonfile:
                data = json.load(jsonfile)
        elif setup == "folderpath":
            with open(base_path, "r") as jsonfile:
                data = json.load(jsonfile)
        jsonfile.close()
        return data


    @staticmethod
    def write_file(format,data):
        base_path = Path(__file__).parent
        if format == 'excel':
            excel_path = os.path.join(base_path / "../../../../data_output/",  "result.csv")
            with open(excel_path, "w", newline='') as csv_file: 
                writer = csv.writer(csv_file, delimiter=',')
                for line in data:
                    writer.writerow(line)

        elif format == 'txt':
            base_path = os.path.join(base_path / "../../../../data_output/",  "result.txt")
            with open(base_path, "w") as text_file:
                for line in data:
                    writer.writerow(line)
            #         f.writelines(["\nSee you soon!", "\nOver and out."])
            # f.close()
