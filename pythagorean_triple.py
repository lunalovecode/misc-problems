#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pythagoreanTriple' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER a as parameter.
#

def pythagoreanTriple(a):
    b, c = 0, 0
    if a % 2 == 0:
        b = ((a ** 2) // 4) - 1
        c = b + 2
    else:
        b = ((a ** 2) - 1) // 2
        c = b + 1
    
    return a, int(b), int(c)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = int(input().strip())

    triple = pythagoreanTriple(a)

    fptr.write(' '.join(map(str, triple)))
    fptr.write('\n')

    fptr.close()
