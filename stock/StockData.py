import pandas as pd


class BaseData(object):
    def __init__(self, label, value, unit, order):
        self.label = label
        self.value = value
        self.unit = unit
        self.order = order

    def __init__(self, **data):
        self.label = data['label']
        self.value = data['value']
        self.unit = data['unit']
        self.order = data['order']

    

class StockData():
        def __init__(self, equity, liabilities, gross_profit, revenue):
            self.__equity = equity
            self.__liabilities = liabilities
            self.__gross_profit = gross_profit
            self.__revenue = revenue

        def __str__(self):
            return 'equity : ' + str(self.__equity) + ', liabilities : ' + str(self.__liabilities) + ' Gross Profit : ' + str(self.__gross_profit) + ' Revenue : ' + str(self.__revenue)