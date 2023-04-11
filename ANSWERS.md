# Answers by Yunu Choi

Included is answers to the examples described in `README.md`, written by Yunu Choi. Please contact Yunu via yoonwoochoi00@gmail.com for further explanations.

<br>

## Example 1 - Stack Tree

### Scenario 1

```
add_example(1)
```

The literal `1` is **valid** and results in printing `Added 1 successfully` because it is of type `int`, not even, and not `33`, which passes all checks.

<br>

### Scenario 2

```
add_example("a")
```

The literal `"a"` is **not valid** because is not of type `int`, but is of type `string`. Other checks including `_check_even()` and `_check_is_not_33()` are not executed because the check `_check_type()` is called before these checks, and raises a `ValueError` which ends the execution.

<br>

### Scenario 3

```
add_example(2)
```

The literal `2` is **not valid** because even though it is of type `int`, but is even. It passes the check `_check_type()`, but encounters an error in `_check_even()`, which prevents it from executing the next check, `_check_is_not_33()`.

<br>

### Scenario 4

```
add_example(33)
```

The literal `33` is **not valid** because even though it is of type `int` and not even, it fails in the check `_check_is_not_33()`.

<br>

### Extra

- Updated error message for `_check_even()`, from `"The value to add may not be even"` to `"The value to add is not even"` to make the error message consistent to error messages from other checks.
- Updated structure for `_check_is_not_33()` to not create an additional variable to store the error message, so it follows the structure of other checks.

---

<br>

## Example 2 - Performance

### add()

```
    def add(self, value_to_add: int):
        """
        Inefficient way of adding a value to a collection.

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
```

<br>

### add2()

```
    def add2(self, value_to_add: int):
        """
        Write your own method for adding a value as efficiently as possible.

        Args:
            value_to_add (int): The value to add
        """
        start = time.time()

        # Remove this line and implement your method
        if value_to_add not in self._data:
            self._data.append(value_to_add)

        end = time.time()

        return end - start, self._data
```

The main difference between `add()` and `add2()` is that `add()` accesses all values in `self._data` to check if it has `value_to_add`, but `add2()` only checks if it has the exact `value_to_add`. Therefore, there is no need to access other values in `add2()`, which results in a greater performance.

<br>

### Extra

- Fixed a typo in `add()` from `"Ineffient"` to `"Inefficient"`.
- Updated description for `add()` as it only adds a single value, not multiple values.

---

<br>

## Example 3 - Inheritance

### Assumptions

- `calculate_post_tax()` returns a rounded value to the nearest cent, same as `calculate_post_tax_weekly()`.

### Extra

- Changed method name from `calculate_weekly()` to `calculate_post_tax_weekly()` for clarity.
- Fixed data type for after tax values from `int` to `float`, as they are rounded to the nearest cent.
- Placed `calculate_post_tax()` before `calculate_post_tax_weekly()`, as `calculate_post_tax_weekly()` class `calculate_post_tax()`.

---

<br>

## Example 4 - Validation

### Boundary cases

- Since the `Person` class has the attribute `overdraft`, 1 plus or minus the sum of `amount` and `overdraft` can be a boundary case as overdraft allows extra amount to be withdrawn from the account.
- `-1` can be a boundary case because it is just below `0`, which is an accepted parameter.

<br>

### Extra

- Removed unused variables created for withdrawals.
- Added success message when test is passed.

---

<br>

## Example 5 - Abstract

I have named the class `System` as it allows users to leave a message and the work `system` was used in one of the error messages. Only one user can leave a message at a time by checking the `current_user` attribute.

<br>

There are two kinds of custom exceptions used in `Class` - `LoginException` and `MessageException`. A `LoginException` is thrown when another is already using the system when a user tries to call the `_login()` method. A `MessageException` is thrown when the `content` parameter passed to `leave_message` has no content, in other words, an empty string (`""`) or `None`.

---

<br>

<div style="text-align: right"> 
    Date completed: 11/04/2023
    <br>
    <br>
    Yunu Choi
    <br>
    yoonwoochoi00@gmail.com
</div>
