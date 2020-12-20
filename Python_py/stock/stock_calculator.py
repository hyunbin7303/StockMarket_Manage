
from pandas_datareader import data as wb
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

#START_DATE =''
#END_DATE = str(datetime.now().strftime('%Y-%m-%d'))

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
    def clean_data(stock_data,start_date, end_date, col):
        weekdays = pd.date_range(start=start_date, end=end_date)
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
    def get_data(ticker, trigger, start_date = None, end_date = None, interval = "1d"):
        if start_date == "" or start_date == None:
            start_date  ='2005-01-01'
        if end_date == "" or end_date == None:
            end_date  =str(datetime.now().strftime('%Y-%m-%d'))
        try:
            datetime.strptime(start_date, '%Y-%m-%d')
            datetime.strptime(end_date, '%Y-%m-%d')
        except:
            print('received date format : ', date_str)
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")
        if interval not in ("1d", "1wk", "1mo"):
            raise AssertionError("For the interval, it needs to be either 1d, 1wk or 1mo.")
        

        try:
            stock_data = wb.DataReader(ticker,'yahoo', start_date, end_date)
            adj_close = stock_calculator.clean_data(stock_data, start_date, end_date, 'Adj Close')
            
            if trigger == 'plot':
                stock_calculator.create_plot(adj_close,ticker)
            elif trigger == 'print':
                print(stock_data)
            else:
                print('no input.')


        except RemoteDataError:
            print('No data found for {t}'.format(t=ticker))


    # TODO : Jongyoon.
    @staticmethod
    def get_peg(ticker, trigger, site_source):
        print('', ticker)
        if site_source == 'yahoo':
            #Write down formula in here.... 
            check = urllib2.urlopen('http://finance.yahoo.com/q/ks?s=' + ticker).read()
            pricebookratio = check.split('Price/Book (mrq):</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
            print('the current {} ratio is : {}'.format(ticker, pricebookratio))
            if float(pricebookratio) < .60:
                print(pricebookratio, 'is letter than 60!')
                
            print(site_source)

        elif site_source  == 'naver':
            print(site_source)
        else:
            print('other source.')


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


    @staticmethod
    def get_alltickers_sp500():
        sp500 = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]
        sp_tickers = sorted(sp500.Symbol.tolist())
        return sp_tickers

    @staticmethod
    def tickers_nasdaq():
        '''Downloads list of tickers currently listed in the NASDAQ'''
        ftp = ftplib.FTP("ftp.nasdaqtrader.com")
        ftp.login()
        ftp.cwd("SymbolDirectory")
        r = io.BytesIO()
        ftp.retrbinary('RETR nasdaqlisted.txt', r.write)
        info = r.getvalue().decode()
        splits = info.split("|")
        tickers = [x for x in splits if "\r\n" in x]
        tickers = [x.split("\r\n")[1] for x in tickers if "NASDAQ" not in x != "\r\n"]
        tickers = [ticker for ticker in tickers if "File" not in ticker]    
        ftp.close()    
        return tickers



    # Not using for now...
    class InvalidStockError(RuntimeError):
        # Error Code in here.
        def __init__(self):
            print('Testing')



