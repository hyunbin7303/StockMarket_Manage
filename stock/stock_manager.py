import getopt
import sys
import argparse
import helper.utils as utils
from stock_calculator import stock_calculator


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

    def perform_operation(self, chosen_operation): 
        try:
            if chosen_operation == "user_mode":
                self.user_mode()
            elif chosen_operation == "all_filter":
                self.all_filter()

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


    def all_filter(self):
        setupFilter = utils.get_config_file('user_settings')['filter']
        tickers = load_all_tickers()
        for ticker in tickers:
            print('INDEX NAME : {}'.format(ticker))
            if setupFilter['peg'] != 'None':
                stock_calculator.get_peg(ticker,'y')
            
            if setupFilter['mg'] != 'None':
                stock_calculator.get_margin(ticker,'y')

            if setupFilter['rev'] != 'None':
                stock_calculator.get_revenue(ticker, 'y')