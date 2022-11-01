import requests
import json
import helper.utils
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
from HistoricData import HistoricData

# Getting the stock information from the user.
class stock_collector:


    def __init__(self):
        self.__username= ''
        self.__enddate = ''
        self.__api_key = 'rFCMKgr8aQAV6tQb8kM6DMK_AgoVw8aq'
        self.__url = 'https://api.polygon.io'
        self.__income_statement =[]
        self.__cashflow_statement = []
        self.__balance_sheet= []

    def get_stocks_from_file(self):
        print ('Test get stock from file.')

    def collect_ticker_data(self, tickers):
        pass
    
    
    def get_ticker_info(self, ticker):
        print('get ticker info')

    def get_historic_data(self, ticker, startdate, enddate) -> list:
        url = f'{self.__url}/v2/aggs/ticker/{ticker}/range/1/day/{startdate}/{enddate}?adjusted=true&sort=asc&limit=100&apiKey={self.__api_key}'
        response =requests.get(url).json()
        df = pd.DataFrame(response['results']).values.tolist()
        return df

    #Comprehensive income is the variation in a company's net assets from non-owner sources during a specific period.
    def get_comprehensive_income(self, ticker):
        pass

    def get_margin(self, ticker): # This is part of the income statement. 
        pass

    

    def load_financials(self, ticker)-> None:
        url = f'{self.__url}/vX/reference/financials?ticker={ticker}&apiKey={self.__api_key}'
        response = requests.get(url).json()
        financials = response['results'][0]['financials']
        self.__income_statement = pd.DataFrame(financials['income_statement']).values.tolist()
        self.__cashflow_statement = pd.DataFrame(financials['cash_flow_statement']).values.tolist()
        self.__balance_sheet = pd.DataFrame(financials['balance_sheet']).values.tolist()
        self.__comprehensive_income = pd.DataFrame(financials['comprehensive_income']).values.tolist()


    def get_income_statement() -> list:
        return self.__income_statement

    def get_cashflow_statement() -> list:
        return self.__cashflow_statement

    def get_balance_sheet() -> list:
        return self.__balance_sheet