from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(frozen=True)
class OrderedLine:
    order_id: str
    SKU: str
    qty: int


@dataclass
class Batch:

    refId: str
    SKU: str
    capability: int
    eta: Optional[date]

    def allocate(self, order_line: OrderedLine):
        self.capability -= order_line.qty