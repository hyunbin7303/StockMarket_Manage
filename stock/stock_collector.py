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

    def get_stocks_from_file(self):
        print ('Test get stock from file.')

    def collect_ticker_data(self, tickers):
        pass
