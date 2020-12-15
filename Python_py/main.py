import getopt
import sys
import argparse
from stock import stock_manage


# Where should I move these fields?... Global is usually bad. 
TICKER =""
START_DAY = ""
END_DAY = ""


# need to update this method to be a class...... 
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
 # ap.add_argument("-a", "--all", type=str, required=False, hlep="Display all stocks.")

  # additional argument that I would like to add:
#   """
#   argParser.add_argument("--top_n", type=int, default = 25, help="How many top predictions do you want to print")
# argParser.add_argument("--min_volume", type=int, default = 5000, help="Minimum volume filter. Stocks with average volume of less than this value will be ignored")
# argParser.add_argument("--history_to_use", type=int, default = 7, help="How many bars of 1 hour do you want to use for the anomaly detection model.")
# argParser.add_argument("--is_load_from_dictionary", type=int, default = 0, help="Whether to load data from dictionary or get it from data source.")
# argParser.add_argument("--data_dictionary_path", type=str, default = "dictionaries/data_dictionary.npy", help="Data dictionary path.")
# argParser.add_argument("--is_save_dictionary", type=int, default = 1, help="Whether to save data in a dictionary.")
# argParser.add_argument("--data_granularity_minutes", type=int, default = 15, help="Minute level data granularity that you want to use. Default is 60 minute bars.")
# argParser.add_argument("--is_test", type=int, default = 0, help="Whether to test the tool or just predict for future. When testing, you should set the future_bars to larger than 1.")
# argParser.add_argument("--future_bars", type=int, default = 25, help="How many bars to keep for testing purposes.")
# argParser.add_argument("--volatility_filter", type=float, default = 0.05, help="Stocks with volatility less than this value will be ignored.")
# argParser.add_argument("--output_format", type=str, default = "CLI", help="What format to use for printing/storing results. Can be CLI or JSON.")
#   """

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
  stock_manage.calculate_AverageReturn(TICKER, 'print_year')


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




