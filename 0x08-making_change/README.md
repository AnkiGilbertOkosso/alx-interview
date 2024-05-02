# Change Making Module

This Python module provides a function for determining the fewest number of coins needed to meet a given total amount, given a pile of coins with different values.

## Function

### `makeChange(coins, total)`

Determines the fewest number of coins needed to meet a given total amount.

#### Arguments

- `coins` (list): A list of coin values.
- `total` (int): The total amount to make change for.

#### Returns

- `int`: The fewest number of coins needed to meet the total. Returns -1 if the total cannot be met by any combination of coins.

## Example Usage

```python
from change_making_module import makeChange

# Example 1
result = makeChange([1, 2, 25], 37)
print(result)  # Output: 7

# Example 2
result = makeChange([1256, 54, 48, 16, 102], 1453)
print(result)  # Output: -1
