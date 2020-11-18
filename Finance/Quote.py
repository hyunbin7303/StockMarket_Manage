import datetime

class Quote:

    something: str
    quoteNum: int
    datetimecheck : datetime.date
    title: str


    def __eq__(self, other):

        return self.__dict__ == other.__dict__

    def __init__(self,
                 something: str = None,
                 quoteNum: int = None,
                 datetimecheck: datetime.date = None,
                 title: str = None):

        self.something = something
        self.quoteNum = quoteNum
        self.datetimecheck = datetimecheck
        self.title = title

    def __len__(self):
        return len(self.title)





