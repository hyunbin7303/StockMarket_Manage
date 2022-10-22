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

        # get user info from here.
        # stock_names = open(self.stock_filePath, "r").readlines()
        # stock_names = [str(item).strip("\n")]

    def collect_ticker_data(self, tickers):
        pass

    def load_all_tickers(self):
        matchers = ['#', '/']
        base_path = Path(__file__).parent
        file_path = (base_path / "../../../../data/stock_list.txt").resolve()
        stocks = open(file_path, "r").readlines()
        stocks = [str(item).strip("\n") for item in stocks]
        element = [x for x in stocks if "#" not in x]
        return list(sorted(set(element)))



class Metric(object):
    """
    A base metric class that accepts points, slices them into time intervals
    and performs roll-ups within those intervals.
    """
    def add_point(self, value):
        """ Add a point to the given metric. """
        raise NotImplementedError()

    def flush(self, timestamp, interval):
        """ Flush all metrics up to the given timestamp. """
        raise NotImplementedError()