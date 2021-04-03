from metricbase import MetricBase


DEFAULT_STOCK = "basic"
DEFAULT_TAG = "A"




class StockMetric(MetricBase):

    def __init__(self, ticker, revenue, margin, peg, ror, rsi):
        # tickers = tickers if isinstance(a)
        self.ticker = ticker
        self.rev = revenue
        self.mg = margin
        self.peg = peg
        self.ror = ror
        self.rsi = rsi


    def add_point(self, value):
        self.value.append(value)

    def flush(self, timestamp, interval):
        return [(timestamp, self.value, self.name, self.tags, self.host, MetricType.Distribution, interval)]


    def get_revenue_info(self, filter):
        pass

    def get_margin_info(self, filter):
        pass

    def get_PEG_info(self, filter):
        pass

    def get_all(self, metric, timestamp = None):
        pass

    def print_rsi_info(self, overbought=0.7, oversold = 0.3):
        print('Current RSI value : ', self.rsi)
        if self.rsi < oversold:
            print ("oversold")
        elif self.rsi >overbought:     
            print  ("overbought")
        else :
            print ("normal")



# This is jsust example of Metric Class.
class CoinMetric(MetricBase):
    def __init__(self, coinname):
        pass