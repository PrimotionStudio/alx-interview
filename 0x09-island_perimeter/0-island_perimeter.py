#!/usr/bin/python3
"""0-island_perimeter.py"""
from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    """
    This function calculates the perimeter
    of an island in a given grid.
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                # check top
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                # check right
                if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1
                # check bottom
                if j < len(grid) - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1
                # check left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
    return perimeter
