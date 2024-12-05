from typing import Callable


CurrencyFormatMixin = Callable[[int], str]


def USD(value: int) -> str:
    return "${:,}.{:02d}".format(value // 100, value % 100)


class Currency:
    def __init__(self, value: int, format: CurrencyFormatMixin):
        super().__init__()
        self.value = value
        self.format = format

    def __str__(self) -> str:
        return self.format(self.value)
