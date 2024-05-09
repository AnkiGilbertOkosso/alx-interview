#!/usr/bin/python3
"""Module for computing the perimeter of an island."""


def island_perimeter(grid):
    """Compute the perimeter of an island with no lakes.

    Args:
        grid (list of list of int): The grid representing the island.

    Returns:
        int: The perimeter of the island.

    """
    perimeter = 0
    if not isinstance(grid, list):
        return 0
    num_rows = len(grid)
    for i, row in enumerate(grid):
        num_cols = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == num_cols - 1 or (num_cols > j + 1 and row[j + 1] == 0),
                i == num_rows - 1 or (len(grid[i + 1]) > j and
                                      grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
