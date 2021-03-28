
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
    def get_peg(ticker, site):
        if site == 'yahoo':
            url_tmpl = 'https://finance.yahoo.com/quote/{ticker}/key-statistics?p={ticker}'.format(ticker=ticker) 
            Raw_data_peg = pd.read_html(url_tmpl, encoding='UTF-8')
            Raw_data_peg=Raw_data_peg[0]
            PEG_raw_peg=Raw_data_peg.loc[[4,5]]
            #print(PEG_raw_peg)
            return PEG_raw_peg



    # 2021-01-01 getmargin(profit/operating)
    @staticmethod
    def get_margin(ticker, site):
        if site == 'yahoo':
            url_tmpl = 'https://finance.yahoo.com/quote/{ticker}/key-statistics?p={ticker}'.format(ticker=ticker) 
            try:
                Raw_data_margin = pd.read_html(url_tmpl, encoding='UTF-8')
                Raw_data_margin = Raw_data_margin[5]
                print(Raw_data_margin) 
                return Raw_data_margin

                Operating_Margin=Raw_data_margin.iloc[[1],[1]]
                Operating_Margin=Operating_Margin.values
                Operating_Margin=Operating_Margin.tolist()
                Operating_Margin=Operating_Margin[0]
                Operating_Margin[0]=float(Operating_Margin[0].replace('%',''))
                # if Operating_Margin[0] >= 20:
                #     print ("Operating_Margin over 20%")
            except Exception as ex:
                print(ex)

    # 2021-01-02 get revenue and check groth 15% per year
    @staticmethod
    def get_revenue(ticker, site):
        if site == 'yahoo':
            url_tmpl = 'https://finance.yahoo.com/quote/{ticker}/analysis?p={ticker}'.format(ticker=ticker) 
            Raw_data_revenue = pd.read_html(url_tmpl, encoding='UTF-8')
            Raw_data_revenue = Raw_data_revenue[1]
            #print(Raw_data_revenue)
            return Raw_data_revenue

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
    def get_rsi(ticker, rsi_period):
        if rsi_period != "":
            url_tmpl = 'https://finance.yahoo.com/quote/{ticker}/history?p={ticker}'.format(ticker=ticker) 
            Raw_data_RSI = pd.read_html(url_tmpl, encoding='UTF-8')
            Raw_data_RSI =Raw_data_RSI[0]
    #extract RSI data refer to rsi_period
            RSI_Raw=Raw_data_RSI.iloc[0:rsi_period]
            RSI_Raw=RSI_Raw.sort_values(by=['Date'], ascending=True)
            np.array(RSI_Raw['Date'].tolist())
            np.array(RSI_Raw['Close*'].tolist())
            RSI_date=list(np.array(RSI_Raw['Date'].tolist()))
            RSI_close=list(np.array(RSI_Raw['Close*'].tolist()))
    #calculate close gap
            RSI_close_gap=[]
            for i in range(len(RSI_close)):
                if i==(len(RSI_close)-1):
                    break
                RSI_close_gap.append(round(float(RSI_close[i+1])-float(RSI_close[i]),2))
    #calculate RSI numer/deno
            RSI_numer=0
            RSI_deno=0
            for i in RSI_close_gap:
                if i<0:
                    RSI_deno+=abs(i)
                else:
                    RSI_deno+=i
                    RSI_numer+=i
            RSI=round(RSI_numer/RSI_deno,2)
            # print (RSI_deno)
            # print (RSI_numer)
            print ("RSI={RSI} ".format(RSI=RSI)) 
            #RSI > 0.7 : overbought, RSI <0.3 : oversold            
            if RSI < 0.3:
                print ("oversold")
            elif RSI >0.7:     
                print ("overbought")
            else :
                print ("normal")
            return RSI         

    @staticmethod
    def get_sed(ticker, SED_gap):
        # windows system date from 1970-01-01.
        START_DATE  ='1970-01-02'
        stock_data = wb.DataReader(ticker,'yahoo', START_DATE, END_DATE)
        stock_data=stock_data.reset_index()
        IPO=stock_data.iloc[0].iloc[0].date()
        SED=stock_data.loc[:,['Date','Close']]
        SED = SED.sort_values(by=['Date'], ascending=False) 
        np.array(SED['Date'].tolist())
        np.array(SED['Close'].tolist())
        SED_date_time=list(np.array(SED['Date'].tolist()))
        SED_Date=[]
        for i in SED_date_time:
            SED_Date.append(i.date())
        SED_Close=list(np.array(SED['Close'].tolist()))
        SED=round(100*(float(SED_Close[0])-float(SED_Close[SED_gap]))/float(SED_Close[0]),2)
        print ("IPO date: {}".format(IPO))
        print("Start({}):({}) End({}):({}) Difference for {} traiding days  is {}%".format(SED_Date[SED_gap],round(SED_Close[SED_gap],2),SED_Date[0],round(SED_Close[0],2),SED_gap,SED))
        return SED            
 
    @staticmethod
    def get_Return_of_Rate(ticker, ror_list):
        stock_data = wb.DataReader(ticker,'yahoo', str(ror_list[0]), str(ror_list[1]))
        stock_data=stock_data.reset_index()
        ROR=stock_data.loc[:,['Date','Close']]
        ROR = ROR.sort_values(by=['Date'], ascending=True) 
        np.array(ROR['Date'].tolist())
        np.array(ROR['Close'].tolist())
        ROR_date_time=list(np.array(ROR['Date'].tolist()))
        ROR_Date=[]
        for i in ROR_date_time:
            ROR_Date.append(i.date())
        ROR_Close=list(np.array(ROR['Close'].tolist()))
        ROR=round(100*(float(ROR_Close[0])-float(ROR_Close[(len(ROR_Date)-1)]))/float(ROR_Close[(len(ROR_Date)-1)]),2)
        print("Return of rate: Start({}):({}) End({}):({}) Difference for {} traiding days  is {}%".format(ror_list[0],round(ROR_Close[0],2),ror_list[1],round(ROR_Close[(len(ROR_Date)-1)],2),len(ROR_Date)-1,ROR))
        return ROR          
        


    @staticmethod
    def calculate_volatility(self):
        print(self)

    @staticmethod 
    def caclulate_EPS(ticker):
#주당순이익이란 1주가 벌어들이는 당기순이익을 의미한다. 당기순이익을 발행주식수로 나누면 된다. 
#        search_value('Earnings Per Share USD', '2019-09')
        print ('a')

    @staticmethod
    def calculate_PER(ticker):
        pass
        
    @staticmethod
    def calculate_AverageReturn(ticker, trigger, start_day = None):
        try:
            startday='2010-1-1'
            if start_day != None:
                startday = start_day
            company = wb.DataReader(ticker, data_source = 'yahoo', start=startday)
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



