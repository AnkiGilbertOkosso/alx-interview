# 2D Matrix Rotation Module

This module provides a function `rotate_2d_matrix` to rotate an m by n 2D matrix in place by 90 degrees clockwise.

## Usage

### Function Signature

```python
def rotate_2d_matrix(matrix):
    """
    Rotates an m by n 2D matrix in place.

    :param matrix: The 2D matrix to rotate.
    :type matrix: list[list[int]]
    """
```

### Input

- `matrix`: The 2D matrix to rotate. It must be represented as a list of lists, where each inner list represents a row of the matrix, and all inner lists must have the same length.

### Output

The function does not return anything. It modifies the input matrix in place.

## Example

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)
print(matrix)
```

Output:

```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## How it Works

The function rotates the matrix layer by layer, starting from the outermost layer and moving towards the center. It iterates through each layer and swaps the elements in a clockwise direction until the entire matrix is rotated.

## Error Handling

- If the input is not a list, the function returns immediately.
- If the input list is empty, the function returns immediately.
- If the input matrix is not rectangular (i.e., not all rows have the same length), the function returns immediately.
