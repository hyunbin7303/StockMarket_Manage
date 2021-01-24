
from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
from helper.utils import utils


class stock_collector:


    def __init__(self):
        self.__username= ''
        self.__enddate = ''

    def get_stocks_from_file(self):
        print ('Test get stock from file.')

        # get user info from here.
        # stock_names = open(self.stock_filePath, "r").readlines()
        # stock_names = [str(item).strip("\n")]

    def collect_ticker_data(self, tickers):
        pass
