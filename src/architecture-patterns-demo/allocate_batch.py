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
    def __init__(self, ref_id, sku, capability, eta):
        self.ref_id = ref_id
        self.sku = sku
        self.capability = capability
        self.eta = eta

    def allocate(self, order_line: OrderedLine):
        self.capability -= order_line.qty

    def deallocated(self, unallocated_line):
        pass
