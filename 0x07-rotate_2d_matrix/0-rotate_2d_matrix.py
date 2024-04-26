#!/usr/bin/python3
"""2D matrix rotation.
"""


def rotate_2d_matrix(matrix):
    """Rotates an n by n 2D matrix in place.
    """
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    rows = len(matrix)
    cols = len(matrix[0])
    if not all(map(lambda x: len(x) == cols, matrix)):
        return
    current_col, current_row = 0, rows - 1
    for i in range(cols * rows):
        if i % rows == 0:
            matrix.append([])
        if current_row == -1:
            current_row = rows - 1
            current_col += 1
        matrix[-1].append(matrix[current_row][current_col])
        if current_col == cols - 1 and current_row >= -1:
            matrix.pop(current_row)
        current_row -= 1
