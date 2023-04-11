import decimal


class Person:
    name: str = ""
    age: int = int

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


class Employee(Person):
    # TODO

    def __init__(self, name: str, age: int, salary: decimal) -> None:
        # TODO: Call base class and instantiate attributes.
        # TODO: Salary is the annual amount paid to an employee
        pass

    def calculate_post_tax_weekly(self) -> decimal:
        """
        Calculate the weekly payment to a worker after taxes."""
        # TODO: Calculate weekly payment to a worker after taxes applied.
        # For simplicity, please use 52 weeks in a year.
        # Please round to the nearest cent.
        pass

    def calculate_post_tax(self) -> decimal:
        """Calculate the tax obligation of an employee."""
        # Apply Tax rates (10.5, 17.5, 30, 33, 39)
        # https://tinyurl.com/y34xm2tv
        # TODO: Calculate the tax obligation of a worker from their salary
        # Use the tax brackets provided in the above link
