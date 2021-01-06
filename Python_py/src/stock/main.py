import getopt
import sys
import argparse

from helper.utils.arg_manager import arg_manager
from helper.utils.utils import utils
from stock_calculator import stock_calculator
def main():
# TODO Automatically read json file in config.
  util = utils()
  util.get_configFile('user')
  
  test = arg_manager()
  test.arg_store(sys.argv)         
  try:
    #stock_calculator.get_data(test.get_ticker(), 'print', test.get_startdate())
    stock_calculator.get_margin(test.get_ticker(),test.get_margin())
    stock_calculator.get_revenue(test.get_ticker(),test.get_revenue())
    #stock_calculator.stock_calculator.get_data(test.get_ticker(), 'plot', test.get_startdate())
    #stock_calculator.calculate_AverageReturn(test.get_ticker(), 'print')
    #stock_calculator.calculate_AverageReturn(test.get_ticker(), 'plot')
    #stock_calculator.calculate_AverageReturn(test.get_ticker(), 'print_year')
  except Exception as ex:
    print(ex)


if __name__ =="__main__":

    #basic config      
    if sys.version_info<(3,5,0):
        sys.stderr.write("You need python 3.5 or later to run this script\n")
        sys.exit(1)

    main()

