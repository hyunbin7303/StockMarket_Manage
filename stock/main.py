import getopt
import sys
import argparse
import helper.utils as util
from typing import Any, List, Dict, TypeVar, Generic

from helper.arg_manager import arg_manager
from helper.dbaccess import DbConnection
from stock_calculator import stock_calculator
from stock_collector import stock_collector
from stock_manager import stock_manager

def main():
  test = arg_manager()
  test.arg_store(sys.argv)   

  dbaccess = DbConnection("127.0.0.1", "postgres", "Master#1234", "5432", "FinanceDiary")
  rows = dbaccess.select_rows("select * from indicators")
  print(rows[0][1])
  # TODO : Insert Data
  # TODO : Update Data

  
  manager = stock_manager()    
  try:
    # Not using this portion at all(for now)
    if test.get_username() != 'None':
      getConfig = get_config_file(test.get_username())
      get_tickers = test.get_option_choose(test.get_username())
      myStocks = []
      for t in get_tickers['tickers']:
        myStocks.append(t['symbol'])     

      for ticker in myStocks:
        print('TICKER NAME : {}'.format(ticker))
        stock_calculator.get_peg(ticker,'yahoo')


    else:
      manager.perform_operation("all_filter", test.get_startdate(), test.get_enddate())
      #x = perform_operation("add", {"to": 4}) # Adds 4
      #stock_calculator.get_data(test.get_ticker(), 'print', test.get_startdate())

  except Exception as ex:
    print("Excetion Happened : " + ex)


if __name__ =="__main__":

    #basic config      
    if sys.version_info<(3,5,0):
        sys.stderr.write("You need python 3.5 or later to run this script\n")
        sys.exit(1)

    main()

