from dataclasses import dataclass

@dataclass
class Stock:

    ticker: str
    company_name:str
    stock_desc: str
    stock_type: str
    stock_sector: str
    stock_exchange: str 
    
    def __init__(self, ticker, company_name, desc, type,sector,exchange):
        self.ticker = ticker
        self.company_name = company_name
        self.stock_desc = desc
        self.stock_type = type
        self.stock_sector = sector
        self.stock_exchange = exchange
        self.stcoknews = {}
