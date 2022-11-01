import requests
import json
import helper.utils
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime


# Getting the stock information from the user.
class stock_collector:


    def __init__(self):
        self.__username= ''
        self.__enddate = ''
        self.__api_key = 'rFCMKgr8aQAV6tQb8kM6DMK_AgoVw8aq'
        self.__url = 'https://api.polygon.io/v2'

    def get_stocks_from_file(self):
        print ('Test get stock from file.')

    def collect_ticker_data(self, tickers):
        pass
    
    
    def get_ticker_info(self, ticker):
        print('get ticker info')

    def get_data(self, ticker, startdate, enddate) -> str:
        url = f'{self.__url}/aggs/ticker/{ticker}/range/1/day/{startdate}/{enddate}?adjusted=true&sort=asc&limit=120&apiKey={self.__api_key}'
        response =requests.get(url).json()
        return response

