import decimal


class Person:
    name: str = ""
    age: int = int

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


class Employee(Person):
    # TODO
    salary: int = int

    def __init__(self, name: str, age: int, salary: decimal) -> None:
        # TODO: Call base class and instantiate attributes.
        # TODO: Salary is the annual amount paid to an employee
        super().__init__(name, age)
        self.salary = salary
        self.salary_post_tax = None

    def calculate_post_tax(self) -> float:
        """Calculate the tax obligation of an employee."""
        # Apply Tax rates (10.5, 17.5, 30, 33, 39)
        # https://tinyurl.com/y34xm2tv
        # TODO: Calculate the tax obligation of a worker from their salary
        # Use the tax brackets provided in the above link
        tax_rate = None

        if self.salary <= 14000:
            self.salary_post_tax = self.salary - (self.salary * 10.5 / 100)

        elif self.salary <= 48000:
            salary_below_bracket = self.salary - 14000
            self.salary_post_tax = self.salary - (1470 + (salary_below_bracket * 17.5 / 100))

        elif self.salary <= 70000:
            salary_below_bracket = self.salary - 48000
            self.salary_post_tax = self.salary - (7420 + (salary_below_bracket * 30 / 100))

        elif self.salary <= 180000:
            salary_below_bracket = self.salary - 70000
            self.salary_post_tax = self.salary - (14020 + (salary_below_bracket * 33 / 100))

        else:
            salary_below_bracket = self.salary - 180000
            self.salary_post_tax = self.salary - (50320 + (salary_below_bracket * 39 / 100))

        return round(self.salary_post_tax, 2)


    def calculate_post_tax_weekly(self) -> float:
        """
        Calculate the weekly payment to a worker after taxes."""
        # TODO: Calculate weekly payment to a worker after taxes applied.
        # For simplicity, please use 52 weeks in a year.
        # Please round to the nearest cent.
        salary = self.calculate_post_tax()

        return round(salary / 52, 2)
