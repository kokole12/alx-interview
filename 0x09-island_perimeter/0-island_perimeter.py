#!/usr/bin/python3
"""Implementing a function to calculate the
perimeter of an Island
Args:
    grid
"""


def island_perimeter(grid):
    """implementing the perimeter calculation"""
    rows = len(grid)
    cols = len(grid[0])

    perimeter = 0

    for r in range(rows):
        for col in range(cols):
            if grid[r][col] == 1:
                perimeter += 4
                if grid[r][col -1] == 1:
                    perimeter -= 2
                if grid[r - 1][col] == 1:
                    perimeter -= 2
    return perimeter
