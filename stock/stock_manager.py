import getopt
import sys
import argparse
import helper.utils as utils
from stock_calculator import stock_calculator
from stock_collector import stock_collector
from HistoricData import BaseData
from pathlib import Path

class stock_manager:




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

    def load_all_tickers(self):
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
            balance = collector.get_balance_sheet()
            print(balance)

            Equity = balance["equity"]
            test = BaseData(Equity['label'], Equity['value'], Equity['unit'], Equity['order'])
            print(test.label)
            
            # test = BaseData(Revenue)
            # datacheck = stock_calculator.get_per(ticker)
            
            # if setupFilter['peg'] != 'None':
            #     stock_calculator.get_peg(ticker,'y')
            
            # if setupFilter['mg'] != 'None':
            #     stock_calculator.get_margin(ticker,'y')

            # if setupFilter['rev'] != 'None':
            #     stock_calculator.get_revenue(ticker, 'y')