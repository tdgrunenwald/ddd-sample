import re
from abc import ABC, abstractclassmethod


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
        groups = re.search(r"^\$(\d*)\.?(\d?\d?)$", repr).groups()

        dollars_str = groups[0]
        dollars = int(dollars_str) if dollars_str else 0

        cents_str = groups[1]
        if cents_str and 1 == len(cents_str):
            cents_str += '0'
        cents = int(cents_str) if cents_str else 0

        return dollars * 100 + cents

    @abstractclassmethod
    def toString(cls, value: int) -> str:
        return "${:,}.{:02d}".format(value // 100, value % 100)


class Currency:
    def __init__(self, value: int, format: CurrencyFormatMixin):
        super().__init__()
        self.value = value
        self.format = format

    def __str__(self) -> str:
        return self.format.toString(self.value)
