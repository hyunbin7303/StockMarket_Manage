
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


class Distribution(Metric):
    """ A distribution metric. """
    stats_tag = "d"
    def __init__(self, name, tags, host):
        self.name = name
        self.tags = tags
        self.host = host
        self.value = []

    def add_point(self, value):
        self.value.append(value)

    def flush(self, timestamp, interval):
        return [(timestamp, self.value, self.name, self.tags, self.host, MetricType.Distribution, interval)]

