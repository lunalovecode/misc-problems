#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    primary = []
    secondary = []
    for i in range(len(arr)):
        primary.append(arr[i][i])
    y = len(arr[0]) - 1
    for x in range(len(arr)):
        secondary.append(arr[x][y])
        y -= 1
    
    return abs(sum(primary) - sum(secondary))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
