import json
import os
import sys
import json
import datetime as dt
class utils:
    # __init() method is called immediately after an instance is created.
    # it takes one parameter, the stream object that we want to use as standard output for the life of the context.
    def __init__(self):
        print('Utilities constroctor.')

    @staticmethod
    def path_test():
        print('This is static method!')

    def path_testing(self):
        print("haha")

    # def __enter__():
    #     print('how it is used')
    

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
    def get_configFile(setup):
        print('setup info.',setup)
        if setup is 'apikey':
            with open("//user//config.json", "r") as jsonfile:
                data = json.load(jsonfile) # Reading the file
            print("Read successful")
            jsonfile.close()
        elif setup is 'folderpath':
            print('folder path info.')
        elif setup is 'user':
            print('read one of the file from user folder.')
        else:
            print('do nothing')