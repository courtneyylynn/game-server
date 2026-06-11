from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

@dataclass
class MiscItem:
    itemId: int = 0
    ingredId: int = 0
    ingredPrice: int = 0
    goldPrice: int = 0
    memberGoldPrice: int = None

    def __post_init__(self):
        if self.memberGoldPrice is None:
            self.memberGoldPrice = self.goldPrice

    @classmethod
    def unpackFromTuple(cls, data: Sequence[int]) -> MiscItem:
        if len(data) != 5:
            raise ValueError(f"Expected 5 values for MiscItem, got {len(data)}")

        return cls(*data)

    def asTuple(self) -> tuple[int, ...]:
        return (
            self.itemId,
            self.ingredId,
            self.ingredPrice,
            self.goldPrice,
            self.memberGoldPrice
        )
