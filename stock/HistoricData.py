import pandas as pd


class BaseData(object):
    def __init__(self, label, value, unit, order):
        self.label = label
        self.value = value
        self.unit = unit
        self.order = order

class HistoricData():
        def __init__(self, open, close, high, low, ts, vol, vwap):
            self.__open = open
            self.__close = close
            self.__high = high
            self.__low = low
            self.__transactions = ts
            self.__volumme = vol
            self.__vwap = vwap



# class StockFinancials():
#     def __init__(self, )


class IncomeStatement(BaseData):
    def __init__(self):
        super().__init__(label, value, unit, order)
    
