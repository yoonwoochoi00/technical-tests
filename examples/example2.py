import traceback

from typing import Any
from examples.assets import performance


def assert_results(
    exec_time1: float, result1: Any, exec_time2: float, result2: Any, test_name: str
) -> None:
    """
    Checks results

    Args:
        exec_time1 (float): First execution time
        result1 (Any): First execution result
        exec_time2 (float): Second execution time
        result2 (Any): Second execution result
    """
    has_issue = False
    try:
        assert exec_time1 > exec_time2, "No time improvement"
    except AssertionError as error:
        print(error)
        print(traceback.print_exc())
        print()
        has_issue = True

    try:
        assert len(result1) == len(result2), "Number of values is unexpected"
    except AssertionError as error:
        print(error)
        print(traceback.print_exc())
        print()
        has_issue = True

    if not has_issue:
        print(f"Passed {test_name}")
    else:
        print(f"Failed {test_name}")
    print()


def scenario1():
    """Checks adding an invalid value"""
    test_class = performance.PerformanceTests()
    exec_time1, result1 = test_class.add(41)
    test_class.reset()
    exec_time2, result2 = test_class.add2(41)

    assert_results(exec_time1, result1, exec_time2, result2, "Scenario 1")


def scenario2():
    """Checks adding a valid value"""
    test_class = performance.PerformanceTests()
    exec_time1, result1 = test_class.add(41454)
    test_class.reset()
    exec_time2, result2 = test_class.add2(41454)

    assert_results(exec_time1, result1, exec_time2, result2, "Scenario 2")


def run():
    """Run the examples.

    In this example we ask you to improve the PerformanceTests class.

    Please describe the improvements you made and why.

    You are allowed to modify the underlying PerformanceTests class, but please add attributes
    instead of overriding existing attributes if you do.

    e.g do not change self._data, but create self._data2 and use this in your example.
    """
    print("EXAMPLE 2".center(80))

    scenario1()
    scenario2()
