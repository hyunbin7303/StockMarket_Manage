import sys
import argparse

from helper.utils.arg_manager import arg_manager
from helper.utils.utils import utils
from stock_calculator import stock_calculator
from stockmetric import StockMetric


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
      check = stock_calculator.get_peg(ticker,'yahoo')

    if setupFilter['mg'] != 'None':
      check2= stock_calculator.get_margin(ticker,'yahoo')

    if setupFilter['rev'] != 'None':
      check3 = stock_calculator.get_revenue(ticker, 'yahoo')

    stock = StockMetric(ticker, check, check2, check3)
    print(stock.peg)
    print(stock.mg)
    print(stock.rev)

    utils.write_file('txt',stock.peg)



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
    "mg":  stock_calculator.get_margin(ticker,site),
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

