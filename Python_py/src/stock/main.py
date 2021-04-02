import sys
import argparse

from cli import main


if __name__ =="__main__":

    #basic config      
    if sys.version_info<(3,5,0):
        sys.stderr.write("You need python 3.5 or later to run this script\n")
        sys.exit(1)

    main()

