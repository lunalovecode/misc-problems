#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    counts = {}
    for a in set(arr):
        counts[a] = arr.count(a)
    
    m = -1
    for x in arr:
        if counts[x] == max(counts.values()):
            m = x
            break
    
    deletions = 0
    for x in arr:
        if x != m:
            deletions += 1
    
    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
