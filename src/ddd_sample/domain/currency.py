import re
from abc import ABC, abstractclassmethod
from typing import Self


class CurrencyFormatMixin(ABC):
    @abstractclassmethod
    def toValue(cls, repr: str) -> int:
        pass

    @abstractclassmethod
    def toString(cls, value: int) -> str:
        pass


class USD(CurrencyFormatMixin):
    @abstractclassmethod
    def toValue(cls, repr: str) -> int:
        repr = repr.strip()
        repr = repr.replace(",", "")
        groups = re.search(r"^(-?)\$(\d*)\.?(\d?\d?)$", repr).groups()

        sign_modifier = -1 if groups[0] and groups[0] == "-" else 1

        dollars_str = groups[1]
        dollars = int(dollars_str) if dollars_str else 0

        cents_str = groups[2]
        if cents_str and 1 == len(cents_str):
            cents_str += '0'
        cents = int(cents_str) if cents_str else 0

        return (dollars * 100 + cents) * sign_modifier

    @abstractclassmethod
    def toString(cls, value: int) -> str:
        sign = "-" if value < 0 else ""
        return "{}${:,}.{:02d}".format(sign, abs(value) // 100, abs(value) % 100)


class Currency:
    def __init__(self, value: int, format: CurrencyFormatMixin):
        super().__init__()
        self.value = value
        self.format = format

    def __str__(self) -> str:
        return self.format.toString(self.value)

    def __add__(self, other) -> Self:
        if isinstance(other, Currency):
            new_value = self.value + other.value
        elif isinstance(other, int):
            new_value = self.value + other
        return Currency(value=new_value, format=self.format)

    def __iadd__(self, other):
        if isinstance(other, Currency):
            self.value = self.value + other.value
        elif isinstance(other, int):
            self.value = self.value + other
        return self

    def __eq__(self, other):
        if not isinstance(other, Currency):
            return False

        return other.value == self.value
