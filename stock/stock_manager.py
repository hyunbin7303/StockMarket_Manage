import getopt
import sys
import argparse
import helper.utils as utils
import helper.dbaccess as dbaccess
from stock_calculator import stock_calculator
from stock_collector import stock_collector
from StockData import BaseData
from StockData import StockData
from pathlib import Path

class stock_manager:


    def __init__(self):
        print("stock manager Constructor")
        # need to initialize Db access

    def average_return(self, test):
        stock_calculator.get_data(test.get_ticker(), 'plot', test.get_startdate())
        stock_calculator.calculate_AverageReturn(test.get_ticker(), 'print')
        stock_calculator.calculate_AverageReturn(test.get_ticker(), 'plot')
        stock_calculator.calculate_AverageReturn(test.get_ticker(), 'print_year')
    
    def invalid_op(x):
        raise Exception("Invalid operation")        

    def user_mode(self):
        print("User mode activate")

    def perform_operation(self, chosen_operation, startdate = None, enddate = None): 
        try:
            if chosen_operation == "user_mode":
                self.user_mode()
            elif chosen_operation == "all_filter":
                self.all_filter(startdate, enddate)

   #         chosen_operation_function = ops.get(chosen_operation, invalid_op)
        except Exception as ex:
            print("Excetion Happened : " + ex)

 #       return chosen_operation_function(**operation_args)

    def perform_filter_methods(ticker, site, chosen_filter, operation_args = None):
        operation_args = operation_args or {}
        ops = {
            "peg" : "year",
            "mg":  stock_calculator.get_margin(ticker,site),
            "rev": stock_calculator.get_revenue(ticker,"y")
        }
        print("getting the PER ratio first.")

    def load_all_tickers(self) -> list:
        try:
            matchers = ['#', '/']
            base_path = Path(__file__).parent
            file_path = (base_path / "../data/stock_list.txt").resolve()
            stocks = open(file_path, "r").readlines()
            stocks = [str(item).strip("\n") for item in stocks]
            element = [x for x in stocks if "#" not in x]
            return list(sorted(set(element)))

        except Exception as ex:
            print("Exception for file handling : " + ex)


    def all_filter(self, startdate, enddate):
        setupFilter = utils.get_config_file('user_settings')['filter']
        tickers = self.load_all_tickers()
        collector = stock_collector()

        for ticker in tickers:
            print('INDEX NAME : {}'.format(ticker))
            #data = collector.get_historic_data(ticker, startdate, enddate)
            collector.load_financials(ticker) 

            income_sm = collector.get_income_statement()
            GrossProfit = BaseData(**income_sm["gross_profit"])
            Revenues = BaseData(**income_sm["revenues"])
            
            balance = collector.get_balance_sheet()
            Equity = BaseData(**balance["equity"])
            Assets = BaseData(**balance["assets"])
            CurrentAssets = BaseData(**balance["current_assets"])
            Liabilities = BaseData(**balance["liabilities"])


            stock = StockData(Equity.value, Liabilities.value, GrossProfit.value, Revenues.value)
            print(stock.__str__())
            # datacheck = stock_calculator.get_per(ticker)
            # Get PEG data

      