





class MetricBase(object):
    """
    A base metric class that accepts points, slices them into time intervals
    and performs roll-ups within those intervals.
    """
    def add_point(self, value):
        """ Add a point to the given metric. """
        raise NotImplementedError()

    def flush(self, timestamp, interval):
        """ Flush all metrics up to the given timestamp. """
        raise NotImplementedError()



    def get_row(self, metric):
        pass

    def get_column(self, metric):
        pass

