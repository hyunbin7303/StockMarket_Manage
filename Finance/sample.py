import http.client
import json
import logging
import sys
from time import sleep


## from gw_utility.book import Book
## from gw_utility.logging import Logging

URL = "apidojo-yahoo-finance-v1.p.rapidapi.com"
RapidAPI_KEY = "7c660e7db2msh6dba68fb0305bc6p1d982cjsn55312d329620"

def read_api_data(param = None):
    try:
        #Use Api call method in here.
        conn = http.client.HTTPConnection(URL)
        headers = {
            'x-rapidapi-host': URL,
            'x-rapidapi-key': RapidAPI_KEY
        }
        # parameters can be defined as a dictionary. These parameters are later parsed down and added to the base url or the api-endpoint.
        # PARAMS = {'address':location}
        #r = requests.get(url = URL, params = PARAMS)
        conn.request("GET", "/stock/v2/get-financials?region=US&symbol=AMRN", headers=headers)
        res = conn.getresponse()
        if res.status ==200:
            print('Success to call. ')
        elif res.status == 404:
            print('Not Found. ')

        data = res.read()

        A=data.decode("utf-8")

        A3=A.replace("\"","\'")
        B=json.loads(A)
        CreateJsonFile(B)
        return B

    except AttributeError as error:
        print(error)


def CreateJsonFile(data):
    try:
        file_path_real= "./jong.json"
        with open(file_path_real, 'w') as outfile1:
            json.dump(data,outfile1,indent=4)

    except FileNotFoundError as fnf_error:## currently not using FIleNotFound, but later maybe.
        print(fnf_error)
    except AssertionError as assert_error:
        print(assert_error)
def Process_Data(data):
    print("Beginning data processing..")
    modified_data = data + "that has been modified."
    sleep(2)
    print("Data processing finished.")
    return modified_data
def GetData_from_web():
    print("Retrieving data from the Web.")
    data = "Data from the web"
    return data
def StoreData_to_database(data):
    print("Writing data to a database")
    print(data)
def main():
    data = read_api_data()
    modified_data =Process_Data(data)
    CreateJsonFile(modified_data)

## Main start from here.
if __name__ =="__main__":
    data = "My data read from the Web"
    print(data)
    modified_data = Process_Data(data)
    print(modified_data)
