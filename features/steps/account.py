from behave import given, when, then
from ddd_sample.domain.account import Account, Transaction
from ddd_sample.domain.currency import USD, Currency

import datetime


@given("an account")
def _(context):
    context.account = Account(format=USD)


@when("the following transactions are applied")
def _(context):
    for row in context.table:
        value = USD.toValue(row["amount"])
        txn = Transaction(
            date=datetime.date.today(),
            amount=Currency(value=value, format=USD)
        )
        context.account.post_transaction(txn)


@then("the balance is $1272.01")
def _(context):
    exp = Currency(value=127201, format=USD)
    assert exp == context.account.balance
