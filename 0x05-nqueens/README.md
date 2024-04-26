# N Queens Solution Finder

This module provides a program to find solutions to the N queens problem, which involves placing N non-attacking queens on an N×N chessboard.

## Problem Description

The N queens problem is the challenge of placing N non-attacking queens on an N×N chessboard. A solution to the problem is a configuration of queens on the board such that no two queens threaten each other.

## Usage

To use the program, run it from the command line with the desired board size as an argument:

```
./nqueens.py N
```

Where `N` is an integer greater than or equal to 4, representing the size of the chessboard.

The program will print every possible solution to the problem, with one solution per line, in the format `[row, column]` for each queen's position.

## Example

```
./nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

## Error Handling

- If the user provides the wrong number of arguments, the program will print `Usage: nqueens N` and exit with status 1.
- If `N` is not an integer, the program will print `N must be a number` and exit with status 1.
- If `N` is less than 4, the program will print `N must be at least 4` and exit with status 1.

## Implementation Details

The program uses backtracking to find all possible solutions to the N queens problem. It iterates through every possible position on the chessboard and checks if placing a queen at that position is safe. If it is safe, the program recursively explores placing queens on subsequent rows. If a solution is found, it is added to the list of solutions.
