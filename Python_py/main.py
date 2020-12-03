from stock import stock_manage

USA_STOCK = 'MSFT'
def main():
    data = "My data read from the Web"
    print(data)
    stock_manage.get_data(USA_STOCK, 'print')



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




