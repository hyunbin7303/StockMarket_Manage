import uuid
from dataclasses import dataclass
from dataclasses import dataclass, field, InitVar
from typing import Optional

@dataclass
class Indicatordata():
    id: uuid =field(init=False)
    value: int
    announced_date: str
    recorded_date: str
    date_source : str
