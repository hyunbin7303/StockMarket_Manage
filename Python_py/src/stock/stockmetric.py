from metricbase import MetricBase


DEFAULT_STOCK = "basic"
DEFAULT_TAG = "A"




class StockMetric(MetricBase):

    def __init__(self, ticker, revenue, margin, peg):
        # tickers = tickers if isinstance(a)
        self.rev = revenue
        self.mg = margin
        self.peg = peg


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

# This is jsust example of Metric Class.
class CoinMetric(MetricBase):
    def __init__(self, coinname):
        pass