from dataclasses import dataclass, field

@dataclass
class Indicator():
    indicator_id: int =field(init=False)
    Index: str
    Name:str
    Desc: str
    Country: str