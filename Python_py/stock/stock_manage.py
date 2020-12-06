
# https://www.youtube.com/watch?v=P1ivPY-PQVw
# https://www.youtube.com/watch?v=9fjs8FeLMJk


from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

START_DATE = '2005-01-01'
END_DATE = str(datetime.now().strftime('%Y-%m-%d'))

def get_stats(stock_data):
    return {
        'last': np.mean(stock_data.tail(1)),
        'short_mean': np.mean(stock_data.tail(20)),
        'long_mean': np.mean(stock_data.tail(200)),
        'short_rolling': stock_data.rolling(window=20).mean(),
        'long_rolling': stock_data.rolling(window=200).mean()
    }

def clean_data(stock_data, col):
    weekdays = pd.date_range(start=START_DATE, end=END_DATE)
    clean_data = stock_data[col].reindex(weekdays)
    return clean_data.fillna(method='ffill')

def create_plot(stock_data, ticker):
    stats = get_stats(stock_data)
    plt.style.use('dark_background')

    plt.subplots(figsize=(12,8))
  #  plt.style.use('dark_background') // order is important.
    plt.plot(stock_data, label=ticker)
    plt.plot(stats['short_rolling'], label='20 day rolling mean')
    plt.plot(stats['long_rolling'], label='200 day rolling mean')
    plt.xlabel('Date')
    plt.ylabel('Adj Close (p)')    
    plt.legend()
    plt.title('Stock Price over Time.')
    plt.show()

def get_data(ticker,trigger):

    try:
        stock_data = data.DataReader(ticker,'yahoo', START_DATE, END_DATE)
        adj_close = clean_data(stock_data, 'Adj Close')
        
        if trigger == 'plot':
            create_plot(adj_close,ticker)
        elif trigger == 'print':
            print(stock_data)
        else:
            print('no input.')


    except RemoteDataError:
        print('No data found for {t}'.format(t=ticker))


def get_return(input, old, new):
    print('Getting the return value')

def read_data_from_excel():
    print("Reading data from Excel files.")

def write_data_to_excel():
    print("Writing data to excel files.")

def write_data_to_db():
    print("Writing data to db.")




class InvalidStockError(RuntimeError):
    # Error Code in here.
    def __init__(self):
        print('Testing')



