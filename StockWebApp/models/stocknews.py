import uuid
from dataclasses import dataclass

@dataclass
class StockNews():
    stock_id: int
    title: str
    news_desc: str
    cause: str
    impact_on_stock : str
    price_before : int
    price_after: int
    news_date: str
    record_date: str