from .currency import Currency, CurrencyFormatMixin

from datetime import date as Date


class Transaction:
    def __init__(self, date: Date, amount: Currency):
        self.date = date
        self.amount = amount


class Account:
    def __init__(self, format: CurrencyFormatMixin):
        self.transactions: list[Transaction] = []
        self.balance = Currency(value=0, format=format)

    def post_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)
        self.balance += transaction.amount
