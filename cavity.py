#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    new_grid = [[*row] for row in grid]
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid) - 1):
            a = [int(grid[y - 1][x]), int(grid[y][x - 1]), int(grid[y + 1][x]), int(grid[y][x + 1]), int(grid[y][x])]

            if max(a) == int(grid[y][x]) and all(z != int(grid[y][x]) for z in a[0:4]):
                new_grid[y][x] = "X"
    for row in new_grid:
        yield "".join(row)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
