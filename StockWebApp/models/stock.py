from dataclasses import dataclass, field

@dataclass
class Stock():
    stock_id: int =field(init=False)
    ticker: str
    company_name:str
    stock_desc: str
    stock_type: str
    stock_sector: str
    stock_exchange: str