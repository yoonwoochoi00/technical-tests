import decimal


class ValidationException(Exception):
    """A exception to be thrown when a validation fails."""

    def __init__(self, message: str) -> None:
        super().__init__()

        self.message = message

    def __str__(self) -> str:
        return self.message


class Person:
    """
    A representation of a persons bank account.

    Args:
        amount(decimal): The amount of money a person has in their account.
        overdraw(decimal): The amount a person may go into deficit with their account.
            The amount a person is allowed to owe the bank.
    """

    def __init__(self, amount: decimal = 0) -> None:
        self.amount = amount
        self.overdraft = 1000

    def _withdraw_validations(self, amount_to_withdraw: decimal) -> bool:
        """
        Validates the withdrawal against this persons bank account.

        Args:
            amount_to_withdraw (decimal): The amount being requested
        """

        # TODO: Add all validations you think are important here
        """
        Exammple

        if amount_to_withdraw > 10:
            error_message = "You may not withdraw more than 10 dollars."
            raise ValidationException(error_message)
        """
        if amount_to_withdraw < 0:
            raise ValidationException("Amount to withdraw cannot be negative.")
        
        elif amount_to_withdraw > self.amount + self.overdraft:
            raise ValidationException("You may not withdraw more than {} dollars.".format(str(self.amount + self.overdraft)))

    def withdraw(self, amount_to_withdraw: decimal) -> decimal:
        """
        Withdraw an amount from this account.

        Returns:
            decimal: The amount remaining in the account.
        """

        self._withdraw_validations(amount_to_withdraw)
        self.amount -= amount_to_withdraw

        return self.amount
