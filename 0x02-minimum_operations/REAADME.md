# Minimum Operations

This module provides a function `minOperations` to compute the fewest number of operations needed to result in exactly `n` H characters.

## Problem Statement

Given a number `n`, where each operation consists of either copying all characters currently on the screen (represented by the letter H) or pasting the characters, calculate the minimum number of operations required to obtain exactly `n` H characters.

## Usage

### Function Signature

```python
def minOperations(n):
    """
    Computes the fewest number of operations needed to result
    in exactly n H characters.

    :param n: The target number of H characters.
    :type n: int
    :return: The fewest number of operations needed.
    :rtype: int
    """
```

### Input

- `n`: The target number of H characters.

### Output

- The function returns an integer representing the fewest number of operations needed to achieve exactly `n` H characters.

## Example

```python
n = 4
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))  # Output: 4

n = 12
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))  # Output: 7
```

## Approach

The function iteratively performs copy and paste operations to achieve the desired number of H characters. It tracks the number of operations performed and returns the result.

## Error Handling

- If the input `n` is not an integer, the function returns 0.
