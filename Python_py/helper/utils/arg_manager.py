
import os
import sys
import json
import datetime as dt
import argparse 


# Construct the argument parser
ap = argparse.ArgumentParser(description="Argument parsing for Stock Manager application.", epilog="Enjoy this application.")
# Add the arguments to the parser
ap.add_argument("-t", "--ticker", type=str, required=True, help="TICKER... Type please")
ap.add_argument("-sd", "--startday", type=str, required=False, help="start day")
ap.add_argument("-ed", "--endday", type=str, required =False, help="end day")
ap.add_argument("-g", "--get", type=int, required =False, help="a")
ap.add_argument("-u", "--username", type=str, required =False, help="User name type")
ap.add_argument("-f", "--file", type=str, required=False, help="Getting all tickers file(should be txt files for now...")
ap.add_argument("-m", "--mine", type=str, required=False, help="Getting my json file from the location.")
ap.add_argument("-a", "--all", type=str, required=False, help="Display all stocks.")

ap.add_argument("-peg", "--peg_site", type=str, required=False, help="yahoo")
ap.add_argument("-mg", "--margin", type=str, required=False, help="y/n")
ap.add_argument("-rev", "--revenue", type=str, required=False, help="y/n")

# additional argument that I would like to add:
# argParser.add_argument("--top_n", type=int, default = 25, help="How many top predictions do you want to print")
# argParser.add_argument("--min_volume", type=int, default = 5000, help="Minimum volume filter. Stocks with average volume of less than this value will be ignored")
# argParser.add_argument("--history_to_use", type=int, default = 7, help="How many bars of 1 hour do you want to use for the anomaly detection model.")
# argParser.add_argument("--is_load_from_dictionary", type=int, default = 0, help="Whether to load data from dictionary or get it from data source.")
# argParser.add_argument("--data_dictionary_path", type=str, default = "dictionaries/data_dictionary.npy", help="Data dictionary path.")
# argParser.add_argument("--is_save_dictionary", type=int, default = 1, help="Whether to save data in a dictionary.")
# argParser.add_argument("--data_granularity_minutes", type=int, default = 15, help="Minute level data granularity that you want to use. Default is 60 minute bars.")
# argParser.add_argument("--is_test", type=int, default = 0, help="Whether to test the tool or just predict for future. When testing, you should set the future_bars to larger than 1.")
# argParser.add_argument("--future_bars", type=int, default = 25, help="How many bars to keep for testing purposes.")
# argParser.add_argument("--volatility_filter", type=float, default = 0.05, help="Stocks with volatility less than this value will be ignored.")
# argParser.add_argument("--output_format", type=str, default = "CLI", help="What format to use for printing/storing results. Can be CLI or JSON.")
#Sample run: #python detection_engine.py --is_test 1 --future_bars 25 --top_n 25 --min_volume 5000 --data_granularity_minutes 60 --history_to_use 14 --is_load_from_dictionary 0 --data_dictionary_path 'dictionaries/feature_dict.npy' --is_save_dictionary 1 --output_format 'CLI'

class arg_manager:

    def __init__(self):
        self.__ticker = ''   
        self.__startdate= '2000-01-01'
        self.__enddate = ''
        self.__output_format= ''
        self.__username =''
        self.__peg_site = ''
        self.__margin =''
        self.__revenue =''
    def cur_directory(self):
        directory_path = str(os.path.dirname(os.path.abspath(__file__)))
        print('Current location : ', directory_path)

    def arg_store(self, args):
        args = vars(ap.parse_args())
        if args['ticker'] != None:
            self.__ticker = str(args['ticker'])

        if args['startday'] != None:
            self.__startdate = str(args['startday'])

        if args['endday'] != None:
            self.__enddate = str(args['endday'])

        if args['username'] != None:
            self.__username = str(args['username'])

        if args['peg_site'] != None:
            self.__peg_site = str(args['peg_site'])
            print(self.__peg_site)

        if args['margin'] != None:
            self.__margin = str(args['margin'])
            print(self.__margin)

        if args['revenue'] != None:
            self.__revenue = str(args['revenue'])
            print(self.__revenue)
        

    def user_setting_json(self):
        print('used for getting user info(Only using json for now)')

    def get_ticker(self):
        print('show something',self.__ticker)
        return self.__ticker

    def get_startdate(self):
        return self.__startdate

    def get_enddate(self):
        return self.__enddate

    def get_username(self):
        return self.__username

    def get_peg_site(self):
        return self.__peg_site
    
    def get_margin(self):
        return self.__margin

    def get_revenue(self):
        return self.__revenue


