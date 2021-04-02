import sys
import argparse

from cli import product_app
from cli import testing_methods

if __name__ =="__main__":

    #basic config      
    if sys.version_info<(3,5,0):
        sys.stderr.write("You need python 3.5 or later to run this script\n")
        sys.exit(1)

    product_app()
    # testing_methods()
