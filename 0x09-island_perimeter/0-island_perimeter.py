#!/usr/bin/python3
"""module docs for 0-island_perimeter.py"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    perimeter = 0
    rows = len(grid)
    columns = len(grid[0]) if rows else 0
    for i in range(rows):
        for j in range(columns):
            # print(f"J = {j}")
            # treat each cell as a square; perimeter of cell == 4l
            perimeter += 4 * grid[i][j]
            # since it's completely surrounded by water
            # 1st row must be zeros
            if i > 0 and i < rows - 1:  # for oda rows
                # print(grid[i][j], grid[i-1][j])
                # deduct breadth if it borders a land horizontally
                perimeter -= grid[i][j] * grid[i-1][j]
                perimeter -= grid[i][j] * grid[i+1][j]
            # if i < rows - 1: perimeter -= grid[i][j] * grid[i+1][j]
            if (j > 0) and (j < columns - 1):
                # deduct length if it borders a land vertically
                perimeter -= grid[i][j] * grid[i][j-1]
                perimeter -= grid[i][j] * grid[i][j+1]
            # if j < columns - 1: perimeter -= grid[i][j] * grid[i][j+1]
    return perimeter
