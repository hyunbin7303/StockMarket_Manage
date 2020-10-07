


from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

START_DATE = '2020-10-01'
END_DATE = str(datetime.now().strftime('%Y-%m-%d'))
USA_Stock = 'MSFT'

def get_data(ticker):
    try:
         stock_data = data.DataReader(ticker,'yahoo',START_DATE, END_DATE)
         print(stock_data)

    except RemoteDataError:
        print('No data found for {t}'.format(t=ticker))

get_data(USA_Stock)