import decimal


class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age


class Employee(Person):
    # TODO

    def __init__(self, name: str, age: int, salary: decimal) -> None:
        # TODO: Call base class and instantiate attributes.
        # TODO: Salary is the annual amount paid to an employee
        super().__init__(name, age)
        self._salary = salary

    def calculate_post_tax(self) -> float:
        """Calculate the tax obligation of an employee."""
        # Apply Tax rates (10.5, 17.5, 30, 33, 39)
        # https://tinyurl.com/y34xm2tv
        # TODO: Calculate the tax obligation of a worker from their salary
        # Use the tax brackets provided in the above link
        tax_rate = None

        if self._salary >= 14000:
            tax_rate = 10.5

        elif self.salary >= 48000:
            tax_rate = 17.5

        elif self.salary >= 70000:
            tax_rate = 30

        elif self.salary >= 180000:
            tax_rate = 33

        else:
            tax_rate = 39

        return round(self._salary - self._salary * tax_rate, 2)


    def calculate_post_tax_weekly(self) -> float:
        """
        Calculate the weekly payment to a worker after taxes."""
        # TODO: Calculate weekly payment to a worker after taxes applied.
        # For simplicity, please use 52 weeks in a year.
        # Please round to the nearest cent.
        salary = self.calculate_post_tax()

        return round(salary / 52)
