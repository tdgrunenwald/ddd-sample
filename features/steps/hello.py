from behave import given, when, then


@given('a currency item in {denomination}')
def _(context, denomination: str):
    context.denomination = denomination


@given('value of {value:d}')
def _(context, value: int):
    context.value = value


@when('the currency is stringified')
def _(context):
    context.string = ''


@then('it matches {pattern}')
def _(context, pattern: str):
    assert context.string == pattern, f"'{context.string}' != '{pattern}'"
