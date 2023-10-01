import uuid
from dataclasses import dataclass, field

@dataclass
class StockNews():
    news_id: uuid =field(init=False)
    stock_id: int
    title: str
    news_desc: str
    cause: str
    impact_on_stock : str
    price_before : int
    price_after: int
    news_date: str
    record_date: str