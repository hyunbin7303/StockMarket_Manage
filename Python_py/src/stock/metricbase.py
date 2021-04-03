





class MetricBase(object):

    OK, WARNING, CRITICAL, UNKNOWN = (0, 1, 2, 3)
    """
    A base metric class that accepts points, slices them into time intervals
    and performs roll-ups within those intervals.
    """

    def __init__(self, name, key, prefix="", tags= {}):
        self.name = name
        self.key = key
        self.prefix = prefix
        self.tags = tags or {}

    def add_point(self, value):
        """ Add a point to the given metric. """
        raise NotImplementedError()

    def flush(self, timestamp, interval):
        """ Flush all metrics up to the given timestamp. """
        raise NotImplementedError()

    def __str__(self):
        return 'metric info(name=%s, key=%s, prefix=%s' % (self.name,self.key,self.prefix)

#The repr() function returns a printable representation of the given object.
    __repr__ = __str__

    def get_row(self, metric):
        pass

    def get_column(self, metric):
        pass