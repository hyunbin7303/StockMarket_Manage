import sys
import argparse

from helper.utils.arg_manager import arg_manager
from helper.utils.utils import utils
from stock_calculator import stock_calculator
from stockmetric import StockMetric

def invalid_op(x):
  raise Exception("Invalid operation")

def user_mode():
    getConfig = utils.get_configFile(test.get_username())
    get_tickers = test.get_option_choose(test.get_username())
    myStocks = []
    for t in get_tickers['tickers']:
        myStocks.append(t['symbol'])     

    for ticker in myStocks:
        print('TICKER NAME : {}'.format(ticker))
        stock_calculator.get_peg(ticker,'yahoo')

def all_filter():
  setupFilter = utils.get_configFile('user_settings')['filter']
  tickers = utils.load_all_tickers()
  for ticker in tickers:
    print('INDEX NAME : {}'.format(ticker))
    if setupFilter['peg'] != 'None':
      peg = stock_calculator.get_peg(ticker,'yahoo')

    if setupFilter['mg'] != 'None':
      margin = stock_calculator.get_margin(ticker,'yahoo')

    if setupFilter['rev'] != 'None':
      revenue = stock_calculator.get_revenue(ticker, 'yahoo')

    if setupFilter['ror'] != 'None':
      return_of_rate = stock_calculator.get_Return_of_Rate(ticker, setupFilter['ror'])

    if setupFilter['rsi'] != 'None':
      rsi = stock_calculator.get_rsi(ticker, setupFilter['rsi'])

    stock = StockMetric(ticker, peg, margin, revenue, return_of_rate,rsi)
    print(stock.peg)
    print(stock.mg)
    print(stock.rev)
    print(stock.ror)
    stock.print_rsi_info()
    #utils.write_file('txt',stock.peg)

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
    "peg" :stock_calculator.get_peg(ticker,site),
    "mg":  stock_calculator.get_margin(ticker,site),
    "rev": stock_calculator.get_revenue(ticker,site),
    "rsi": stock_calculator.get_rsi(ticker, ''),
    '': stock_calculator.get_Return_of_Rate(ticker,'')
  }


def main():
    product_app()
   # testing_methods()

def product_app():
    test = arg_manager()
    test.arg_store(sys.argv)         
    try:
        if test.get_username() != 'None':
            perform_operation("user_mode")

        else:
            perform_operation("all_filter")
    #x = perform_operation("add", {"to": 4}) # Adds 4

    except Exception as ex:
        print(ex)

def testing_methods():
    test = arg_manager()
    test.arg_store(sys.argv)         
    #stock_calculator.get_sed(test.get_ticker(),test.get_sed_gap())
    stock_calculator.get_Return_of_Rate(test.get_ticker(),test.get_return_of_rate())
    #stock_calculator.get_data(test.get_ticker(), 'print', test.get_startdate())