import uuid
from dataclasses import dataclass

@dataclass
class Indicatordata():
    value: int
    announced_date: str
    recorded_date: str
    date_source : str
