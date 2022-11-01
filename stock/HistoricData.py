import pandas as pd


class BaseData():
    def __init__(self, label, value, unit, order):
        self.__label = label
        self.__value = value
        self.__unit = unit
        self.__order = order

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
    
