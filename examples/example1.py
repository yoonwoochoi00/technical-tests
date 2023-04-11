import traceback

from typing import Any
from examples.assets import stacktrace


def add_example(value: Any) -> None:
    """Examples where we invoke the add function."""
    try:
        test_class = stacktrace.ErrorTracing()
        test_class.add(value)
    except Exception as e:
        print(e)
        print(traceback.print_exc())
        print()


def run():
    """Run the examples.

    For each of these lines, determine if the code runs, and if it does not
    describe the reason it does not.

    # Does it run?
    # If it does not, why not?
    """
    print("EXAMPLE 1".center(80))
    add_example(1)
    add_example("a")
    add_example(2)
    add_example(33)
