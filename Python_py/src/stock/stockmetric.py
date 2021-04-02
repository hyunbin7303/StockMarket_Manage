from metricbase import MetricBase

class StockMetric(MetricBase):

    def __init__(self, ticker, revenue, margin, peg):
        # tickers = tickers if isinstance(a)
        self.rev = revenue
        self.mg = margin
        self.peg = peg

    stats_tag = "d"

    def add_point(self, value):
        self.value.append(value)

    def flush(self, timestamp, interval):
        return [(timestamp, self.value, self.name, self.tags, self.host, MetricType.Distribution, interval)]


# This is jsust example of Metric Class.
class CoinMetric(MetricBase):
    def __init__(self, coinname):
        pass