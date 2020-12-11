import getopt
import sys
import argparse
from stock import stock_manage



TICKER =""
START_DAY = ""
END_DAY = ""

def argparse_testing():
  if len(sys.argv)> 10:
    print('Too much arguemnts')
    sys.exit()

  # Construct the argument parser
  ap = argparse.ArgumentParser(description="Argument parsing for Stock Manager application.", epilog="Enjoy this application.")
  # Add the arguments to the parser
  ap.add_argument("-t", "--ticker", type=str, required=True, help="TICKER... Type please")
  ap.add_argument("-sd", "--startday", type=str, required=False, help="start day")
  ap.add_argument("-ed", "--endday", type=str, required =False, help="end day")
  ap.add_argument("-g", "--Get", type=int, required =False, help="a")
  ap.add_argument("-f", "--file", type=str, required=False, help="Getting all tickers file(should be txt files for now...")
  args = vars(ap.parse_args())
  print('The ticker is ', args['ticker'])
  
  global TICKER
  TICKER = str(args['ticker'])


  if args['startday'] != None:
    global START_DAY
    START_DAY = str(args['startday'])

  if args['endday'] != None:
    global END_DAY
    END_DAY = str(args['endday'])



def main():
  
  argparse_testing()
  print(TICKER)
  stock_manage.get_data(TICKER, 'print', START_DAY)
  stock_manage.get_data(TICKER, 'plot', START_DAY)

  # create command line for Average Return!
  stock_manage.calculate_AverageReturn(TICKER, 'print')
  stock_manage.calculate_AverageReturn(TICKER, 'plot')

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




