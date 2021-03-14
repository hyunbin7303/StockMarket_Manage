




class MetricBase(object):
    """Metric template class."""
    _language = None
    _metrics = None

    def __init__(self, *args, **kwds ):
        pass

    def reset(self):
        """
        Reset the processor.
        Implement this in case you need to reset the processor for each key.
        """
        pass






class Metric(object):
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


class Distribution(Metric):
    """ A distribution metric. """
    stats_tag = "d"
    def __init__(self, name, tags, host):
        self.name = name
        self.tags = tags
        self.host = host
        self.value = []

    def add_point(self, value):
        self.value.append(value)

    def flush(self, timestamp, interval):
        return [(timestamp, self.value, self.name, self.tags, self.host, MetricType.Distribution, interval)]

