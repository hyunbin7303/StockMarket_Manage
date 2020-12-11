import getopt
import sys
import argparse
from stock import stock_manage



TICKER =""
START_YEAR = 0
END_YEAR = 0

def argparse_testing():
  if len(sys.argv)> 10:
    print('Too much arguemnts')
    sys.exit()

  # Construct the argument parser
  ap = argparse.ArgumentParser(description="Argument parsing for Stock Manager application.", epilog="Enjoy this application.")
  # Add the arguments to the parser
  ap.add_argument("-t", "--ticker", type=str, required=True, help="TICKER... Type please")
  ap.add_argument("-sy", "--startYear", type=int, required=False, help="start year")
  ap.add_argument("-ey", "--endYear", type=int, required =False, help="end year")
  ap.add_argument("-f", "--file", type=str, required=False, help="Getting all tickers file(should be txt files for now...")
  args = vars(ap.parse_args())
  print('The ticker is ', args['ticker'])
  


  global TICKER
  TICKER = str(args['ticker'])


  # if statement for checking.
  #global START_YEAR
  #START_YEAR = int(args['startYear'])


  #if st atement for checking.
  #global END_YEAR
  #END_YEAR = int(args['endYear'])

def main():
  
  argparse_testing()
  print(TICKER)
  stock_manage.get_data(TICKER, 'print')
  stock_manage.get_data(TICKER, 'plot')
  #  stock_manage.calculate_AverageReturn('MSFT', 'print')
  #  stock_manage.calculate_AverageReturn('MSFT', 'plot')

## Main start from here.
if __name__ =="__main__":
    main()




# Python modular import has 2 options
# 1. Absolute modular imports
# 2. Relative modular imports.



# When we use relative modular imports, we should stay outside the package and call.
# Python -m myPackage.subPck...~~

# __init__.py files are required to make Python treat the directories as containing packages.
# This is done tp prevent directories with a common name, such as string, ...




