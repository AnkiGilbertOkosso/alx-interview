#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys

solutions = []
"""The list of possible solutions to the N queens problem.
"""
board_size = 0
"""The size of the chessboard.
"""
positions = None
"""The list of possible positions on the chessboard.
"""


def get_input():
    """Retrieves and validates the program's argument.

    Returns:
        int: The size of the chessboard.
    """
    global board_size
    board_size = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        board_size = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)
    return board_size


def is_attacking(position0, position1):
    """Checks if the positions of two queens are in an attacking mode.

    Args:
        position0 (list or tuple): The first queen's position.
        position1 (list or tuple): The second queen's position.

    Returns:
        bool: True if the queens are in an attacking position, else False.
    """
    if (position0[0] == position1[0]) or (position0[1] == position1[1]):
        return True
    return abs(position0[0] - position1[0]) == abs(
        position0[1] - position1[1])


def group_exists(group):
    """Checks if a group exists in the list of solutions.

    Args:
        group (list of integers): A group of possible positions.

    Returns:
        bool: True if it exists, otherwise False.
    """
    global solutions
    for solution in solutions:
        count = 0
        for solution_pos in solution:
            for group_pos in group:
                if solution_pos[
                        0] == group_pos[
                        0] and solution_pos[
                            1] == group_pos[1]:
                    count += 1
        if count == board_size:
            return True
    return False


def build_solution(row, group):
    """Builds a solution for the N queens problem.

    Args:
        row (int): The current row in the chessboard.
        group (list of lists of integers): The group of valid positions.
    """
    global solutions
    global board_size
    if row == board_size:
        temp_group = group.copy()
        if not group_exists(temp_group):
            solutions.append(temp_group)
    else:
        for col in range(board_size):
            index = (row * board_size) + col
            matches = zip(list([positions[index]]) * len(group), group)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(positions[index].copy())
            if not any(used_positions):
                build_solution(row + 1, group)
            group.pop(len(group) - 1)


def get_solutions():
    """Gets the solutions for the given chessboard size.
    """
    global positions, board_size
    positions = list(map(lambda x: [
        x // board_size, x % board_size], range(board_size ** 2)))
    row = 0
    group = []
    build_solution(row, group)


board_size = get_input()
get_solutions()
for solution in solutions:
    print(solution)
