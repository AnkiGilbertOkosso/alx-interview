#!/usr/bin/python3
"""
A module for generating Pascal's triangle.

This module provides a function to create a list of lists representing
Pascal's triangle for a given non-negative integer.

Usage:
    from pascals_triangle import pascal_triangle
    triangle = pascal_triangle(n)
"""


def pascal_triangle(num_rows):
    """
    Generates Pascal's triangle up to the specified row.

    Args:
        num_rows (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list of lists: A list of lists representing Pascal's triangle.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    triangle = []

    if not isinstance(num_rows, int) or num_rows <= 0:
        return triangle

    for row_num in range(num_rows):
        row = []

        for col_num in range(row_num + 1):
            if col_num == 0 or col_num == row_num:
                row.append(1)
            elif row_num > 0 and col_num > 0:
                row.append(
                        triangle[row_num - 1][col_num - 1] +
                        triangle[row_num - 1][col_num])
        triangle.append(row)

    return triangle
