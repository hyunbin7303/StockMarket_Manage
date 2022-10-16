import getopt
import sys
import argparse

from helper.utils.arg_manager import arg_manager
from helper.utils.utils import utils
from stock_calculator import stock_calculator
from stock_collector import stock_collector

def average_return(self, test):
  stock_calculator.get_data(test.get_ticker(), 'plot', test.get_startdate())
  stock_calculator.calculate_AverageReturn(test.get_ticker(), 'print')
  stock_calculator.calculate_AverageReturn(test.get_ticker(), 'plot')
  stock_calculator.calculate_AverageReturn(test.get_ticker(), 'print_year')
     
def invalid_op(x):
  raise Exception("Invalid operation")
def user_mode():
  pass
def all_filter():
  setupFilter = utils.get_configFile('user_settings')['filter']
  tickers = utils.load_all_tickers()
  for ticker in tickers:
    print('INDEX NAME : {}'.format(ticker))
    if setupFilter['peg'] != 'None':
      stock_calculator.get_peg(ticker,'y')
    
    if setupFilter['mg'] != 'None':
      stock_calculator.get_margin(ticker,'y')


    if setupFilter['rev'] != 'None':
      stock_calculator.get_revenue(ticker, 'y')
def invalid_op(x):
  raise Exception("Invalid operation")
def perform_operation(chosen_operation, operation_args=None): 
  # If operation_args wasn't provided (i.e. it is None), set it to be an empty dictionary
  operation_args = operation_args or {}
  ops = {
    "user_mode" : user_mode,
    "all_filter": all_filter
  }
  chosen_operation_function = ops.get(chosen_operation, invalid_op)
  return chosen_operation_function(**operation_args)
# Need to update this method... Not using it currently.
def perform_filter_methods(ticker, site, chosen_filter, operation_args = None):
  operation_args = operation_args or {}
  ops = {
    "peg" : "year",
    "mg":stock_calculator.get_margin(ticker,site),
    "rev": stock_calculator.get_revenue(ticker,"y")
  }
def main():
  test = arg_manager()
  test.arg_store(sys.argv)         
  try:
    
    if test.get_username() != 'None':
      getConfig = utils.get_configFile(test.get_username())
      get_tickers = test.get_option_choose(test.get_username())
      myStocks = []
      for t in get_tickers['tickers']:
        myStocks.append(t['symbol'])     

      for ticker in myStocks:
        print('TICKER NAME : {}'.format(ticker))
        stock_calculator.get_peg(ticker,'yahoo')


    else:
      perform_operation("all_filter")
      #x = perform_operation("add", {"to": 4}) # Adds 4
      #stock_calculator.get_data(test.get_ticker(), 'print', test.get_startdate())

  except Exception as ex:
    print(ex)


if __name__ =="__main__":

    #basic config      
    if sys.version_info<(3,5,0):
        sys.stderr.write("You need python 3.5 or later to run this script\n")
        sys.exit(1)

    main()

