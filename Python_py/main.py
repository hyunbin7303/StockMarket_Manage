import getopt
import sys
import argparse
from stock import stock_calculator
from helper.utils.arg_manager import arg_manager

def main():
  test = arg_manager()
  test.arg_store(sys.argv)         
  try:
    stock_calculator.stock_calculator.get_data(test.get_ticker(), 'print', test.get_startdate())
    stock_calculator.stock_calculator.get_peg(test.get_ticker(), '')


    #checking
    stock_calculator.stock_calculator.get_data(test.get_ticker(), 'plot', test.get_startdate())
    stock_calculator.calculate_AverageReturn(test.get_ticker(), 'print')
    stock_manage.calculate_AverageReturn(TICKER, 'plot')
    stock_manage.calculate_AverageReturn(TICKER, 'print_year')

  except Exception as ex:
    print(ex)
  
  # except NameError:
  #   print ("name Error")

if __name__ =="__main__":

    #basic config      
    if sys.version_info<(3,5,0):
        sys.stderr.write("You need python 3.5 or later to run this script\n")
        sys.exit(1)

    main()

# When we use relative modular imports, we should stay outside the package and call.
# Python -m myPackage.subPck...~~

# __init__.py files are required to make Python treat the directories as containing packages.
# This is done tp prevent directories with a common name, such as string, ...



# Please use Operator Overloading.
