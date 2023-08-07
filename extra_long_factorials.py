#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Let's see if it can handle this...
    ct = n
    for i in range(n - 1, 0, -1):
        ct *= i
    print(ct)
    # ...wow.
    

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
