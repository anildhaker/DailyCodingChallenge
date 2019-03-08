# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

# Example:

# Input:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Output: 16


class Solution:
    def islandPerimeter(self, grid):
        h = len(grid)
        w = len(grid[0])
        extended_grid = [[0]*(w+2)] + [[0] + row + [0] for row in grid] + [[0]*(w+2)]
        perimeter = 0
        for i in range(h+1):
            for j in range(w+1):
                if extended_grid[i][j] != extended_grid[i][j+1]:
                    perimeter += 1
                if extended_grid[i][j] != extended_grid[i+1][j]:
                    perimeter += 1
        return perimeter
        