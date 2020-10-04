import http.client
import json
import logging
import sys
from time import sleep
## from gw_utility.book import Book
## from gw_utility.logging import Logging

def test():

    try:
        file_path_real= "./jong.json"
        conn = http.client.HTTPConnection("apidojo-yahoo-finance-v1.p.rapidapi.com")
        headers = {
            'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
            'x-rapidapi-key': "7c660e7db2msh6dba68fb0305bc6p1d982cjsn55312d329620"
            }

        conn.request("GET", "/stock/v2/get-financials?region=US&symbol=AMRN", headers=headers)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))
        A=data.decode("utf-8")

        A3=A.replace("\"","\'")
        B=json.loads(A)
        print (B)
        with open(file_path_real, 'w') as outfile1:
            json.dump(B,outfile1,indent=4)

    except AttributeError as error:
        print(error)


def Process_Data(data):
    print("Beginning data processing..")
    modified_data = data + "that has been modified."
    sleep(2)
    print("Data processing finished.")
    return modified_data



if __name__ =="__main__":
    data = "My data read from the Web"
    print(data)
    modified_data = Process_Data(data)
    print(modified_data)




