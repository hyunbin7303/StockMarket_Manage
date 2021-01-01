
from pandas_datareader import data as wb
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

START_DATE =''
END_DATE = str(datetime.now().strftime('%Y-%m-%d'))

class stock_calculator:
    def __init__(self):
        print('stock calculator.')

    @staticmethod
    def get_stats(stock_data):
        return {
            'last': np.mean(stock_data.tail(1)),
            'short_mean': np.mean(stock_data.tail(20)),
            'long_mean': np.mean(stock_data.tail(200)),
            'short_rolling': stock_data.rolling(window=20).mean(),
            'long_rolling': stock_data.rolling(window=200).mean()
        }

    @staticmethod
    def clean_data(stock_data, col):
        weekdays = pd.date_range(start=START_DATE, end=END_DATE)
        clean_data = stock_data[col].reindex(weekdays)
        return clean_data.fillna(method='ffill')

    ## Styling can be the global in some cases.... Please consider line 5~7.
    @staticmethod
    def create_plot(stock_data, ticker):
        stats = stock_calculator.get_stats(stock_data)
        plt.style.use('dark_background')
        plt.subplots(figsize=(12,8))
        #plt.style.use('dark_background') #order is important.
        plt.plot(stock_data, label=ticker)
        plt.plot(stats['short_rolling'], label='20 day rolling mean')
        plt.plot(stats['long_rolling'], label='200 day rolling mean')
        plt.xlabel('Date')
        plt.ylabel('Adj Close (p)')    
        plt.legend()
        plt.title('Stock Price over Time.')
        plt.show()
   
    @staticmethod
    def get_data(ticker,trigger, start_day = None):
        if start_day == "" or start_day == None:
            start_day  ='2005-01-01'

        if start_day != None:
            global START_DATE
            START_DATE = start_day

        try:
            stock_data = wb.DataReader(ticker,'yahoo', START_DATE, END_DATE)
            adj_close = stock_calculator.clean_data(stock_data, 'Adj Close')
            
            if trigger == 'plot':
                stock_calculator.create_plot(adj_close,ticker)
            elif trigger == 'print':
                print(stock_data)
            else:
                print('no input.')


        except RemoteDataError:
            print('No data found for {t}'.format(t=ticker))

    @staticmethod
    def get_peg(ticker, peg_site):
 #       print('aaa{ticker}'.format(ticker))
        if peg_site != "":    
            if peg_site == 'yahoo':
                url_tmpl = 'https://finance.yahoo.com/quote/{ticker}/key-statistics?p={ticker}'.format(ticker=ticker) 
                Raw_data_peg = pd.read_html(url_tmpl, encoding='UTF-8')
                Raw_data_peg=Raw_data_peg[0]
                PEG_raw_peg=Raw_data_peg.loc[[4,5]]
                print(PEG_raw_peg)
            elif peg_site  == 'naver':
                print(peg_site)
            else:
                print('other source.')

    # 2021-01-01 getmargin(profit/operating)
    @staticmethod
    def get_margin(ticker, margin):
        if margin != "":
            if margin == 'y':
                url_tmpl = 'https://finance.yahoo.com/quote/{ticker}/key-statistics?p={ticker}'.format(ticker=ticker) 
                Raw_data_margin = pd.read_html(url_tmpl, encoding='UTF-8')
                Raw_data_margin = Raw_data_margin[5]
                print(Raw_data_margin) 
                Operating_Margin=Raw_data_margin.iloc[[1],[1]]
                Operating_Margin=Operating_Margin.values
                Operating_Margin=Operating_Margin.tolist()
                Operating_Margin=Operating_Margin[0]
                Operating_Margin[0]=float(Operating_Margin[0].replace('%',''))
                if Operating_Margin[0] >= 20:
                    print ("Operating_Margin over 20%")
            else:
                print('insert y or n')
 
    # 2021-01-02 get revenue and check groth 15% per year
    @staticmethod
    def get_revenue(ticker, revenue):
        if revenue != "":
            if revenue == 'y':
                url_tmpl = 'https://finance.yahoo.com/quote/{ticker}/analysis?p={ticker}'.format(ticker=ticker) 
                Raw_data_revenue = pd.read_html(url_tmpl, encoding='UTF-8')
                Raw_data_revenue = Raw_data_revenue[1]
                print(Raw_data_revenue)
    #extract current Growth and convert the format from dp to list
                Current_Growth=Raw_data_revenue.iloc[[5],[3]]
                Current_Growth=Current_Growth.values
                Current_Growth=Current_Growth.tolist()
                Current_Growth=Current_Growth[0]
                Current_Growth[0]=float(Current_Growth[0].replace('%',''))
                if Current_Growth[0] >= 15:
                    print ("Current Growth over 15%")
            else:
                print('insert y or n')
    @staticmethod
    def calculate_volatility(self):
        print(self)
    
    @staticmethod
    def calculate_AverageReturn(ticker, trigger):
        try:
            company = wb.DataReader(ticker, data_source = 'yahoo', start='2010-1-1')
            company['simple_return'] = (company['Adj Close']/ company['Adj Close'].shift(1)) -1
            if trigger == 'plot':
                company['simple_return'].plot(figsize=(8,5))
            elif trigger == 'print':
                print(company['simple_return'])
                avg_returns_d = company['simple_return'].mean()
                print(avg_returns_d) # per day.

            elif trigger == 'print_year':
                print('print year : ')
                avg_returns_annual= company['simple_return'].mean() * 250
                print(avg_returns_annual)
                print(str(round(avg_returns_annual, 5) *100) + ' %')

            elif trigger =='log':
                company['log_return'] = np.log(company['Adj Close']/ company['Adj Close'].shift(1))
                print(company['log_return'])

            else:
                print('no input.')
            

        except RemoteDataError:
            print('No data found for {t}'.format(t=ticker))

    @staticmethod
    def get_return(input, old, new):
        print('Getting the return value')

    @staticmethod
    def read_data_from_excel():
        print("Reading data from Excel files.")

    @staticmethod
    def write_data_to_excel():
        print("Writing data to excel files.")

    @staticmethod
    def write_data_to_db():
        print("Writing data to db.")

    # Not using for now...
    class InvalidStockError(RuntimeError):
        # Error Code in here.
        def __init__(self):
            print('Testing')



