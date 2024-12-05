from behave import given, when, then
from ddd_sample.domain.currency import USD, Currency


@given('a currency item in {denomination}')
def _(context, denomination: str):
    assert denomination == 'USD-cents', f"Denomination '{denomination}' is currently unsupported"
    context.format = USD


@given('value of {value:d}')
def _(context, value: int):
    context.currency = Currency(value=value, format=context.format)


@when('the currency is stringified')
def _(context):
    context.string = str(context.currency)


@then('it matches {pattern}')
def _(context, pattern: str):
    assert context.string == pattern, f"'{context.string}' != '{pattern}'"
