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
        match = re.search(r"^\$(\d*)\.?(\d?\d?)$", repr)
        print(match.groups())
#        dollars = int(match.group(1))
#        cents = int(match.group(2))

        return 0#dollars * 100 + cents

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
