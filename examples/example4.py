import decimal

from examples.assets import validation


def scenario1() -> None:
    """Valid withdrawal"""
    print("Scenario 1")
    bank_value: decimal = 10000
    person = validation.Person(bank_value)
    result = person.withdraw(bank_value)

    expected_result: decimal = 0
    assert result == expected_result, "The withdrawal logic seems incorrect"


def scenario2() -> None:
    """Invalid withdrawal"""
    print("Scenario 2")
    bank_value: decimal = 10000
    person = validation.Person(bank_value)
    try:
        person.withdraw(bank_value + 2000)
    except validation.ValidationException:
        print("Pass - Valid exception raised")
    except Exception:
        print("Failed - Unexpected exception raised.")
    print()


def scenario3() -> None:
    """Invalid withdrawal"""
    print("Scenario 3")
    bank_value: decimal = 10000
    person = validation.Person(bank_value)
    try:
        person.withdraw(-1)
    except validation.ValidationException:
        print("Pass - Valid exception raised")
    except Exception:
        print("Failed - Unexpected exception raised.")
    print()


def run():
    """Run the examples.

    In this example we ask you to improve validations for the validations.Person class.

    In this case we expect you to implement sensible boundary test conditions, as well
    as any validations you believe would be reasonable.

    Validations should raise the exception included in validation.py
    """
    print("EXAMPLE 4".center(80))

    scenario1()
    scenario2()
    scenario3()
