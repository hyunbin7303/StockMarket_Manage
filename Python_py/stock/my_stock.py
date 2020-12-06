# import os
# import sys
# import json
from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
from helper.utils import utils


class StockManager:
    def __init__(self):
        print('Testing')

    def get_stocks_from_file(self):
        print ('Test get stock from file.')
        # stock_names = open(self.stock_filePath, "r").readlines()
        # stock_names = [str(item).strip("\n")]


   # def get_my_data(self, ticker):