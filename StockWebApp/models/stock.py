from dataclasses import dataclass

@dataclass
class Stock():
    ticker: str
    company_name:str
    stock_desc: str
    stock_type: str
    stock_sector: str
    stock_exchange: str
    related_stocknews: []