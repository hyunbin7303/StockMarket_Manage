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

def main():

  test = arg_manager()
  test.arg_store(sys.argv)         
  try:
    
    if test.get_username() != 'None': # -u kevin 
      utils.get_configFile(test.get_username())
      get_userchoose = test.get_option_choose(test.get_username())
      for ticker in get_userchoose:
        print(ticker)
      #run this in order to see the whole tickers.
      # for i in get_userchoose:
      #
      # get all ticker.
      # for ticker in tickcers:
      #       stock_calculator.get_data(ticker, 'print', test.get_startdate())
      #       #stock_calculator.get_peg(ticker,test.get_peg_site())

    else:
      stock_calculator.get_data(test.get_ticker(), 'print', test.get_startdate())
      stock_calculator.get_peg(test.get_ticker(),test.get_peg_site())
      stock_calculator.get_margin(test.get_ticker(),test.get_margin())
      stock_calculator.get_revenue(test.get_ticker(),test.get_revenue())
      #average_return(test)

  except Exception as ex:
    print(ex)


if __name__ =="__main__":

    #basic config      
    if sys.version_info<(3,5,0):
        sys.stderr.write("You need python 3.5 or later to run this script\n")
        sys.exit(1)

    main()

