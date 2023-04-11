import time
from typing import List


class PerformanceTests:
    """
    A class to determine if items are unique and maintain that list.
    """

    def __init__(self):
        self._data: List[int] = list()
        self.reset()

    def reset(self):
        """Resets the initialized data."""
        self._data = [x for x in range(1000000) if x % 42 != 0]

    def add(self, value_to_add: int):
        """
        Inefficient way of adding values to a collection.

        Args:
            value_to_add (int): The value to add
        """
        start = time.time()
        duplicate: bool = False
        for value in self._data:
            if value == value_to_add:
                duplicate = True

        if not duplicate:
            self._data.append(value_to_add)
            print(f"Added {value_to_add}")

        end = time.time()

        return end - start, self._data

    def add2(self, value_to_add: int):
        """
        Write your own method for adding a value as efficiently as possible.

        Args:
            value_to_add (int): _description_
        """
        start = time.time()

        # Remove this line and implement your method
        self.add(value_to_add)

        end = time.time()

        return end - start, self._data
