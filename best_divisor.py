#!/bin/python3

import math
import os
import random
import re
import sys

def get_factors(num):
    factors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            if i != num // i:
                factors.append(num // i)
    factors.sort()
    return factors

if __name__ == '__main__':
    n = int(input().strip())
    x = get_factors(n)
    max_factor = 1
    for y in x:
        if sum([int(z) for z in str(y)]) > max_factor:
            max_factor = sum([int(z) for z in str(y)])
    
    for y in x:
        if sum([int(z) for z in str(y)]) == max_factor:
            print(y)
            break