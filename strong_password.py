#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    has_nums, has_lower, has_upper, has_special_chars, long_enough = False, False, False, False, False
    needed = 0
    if any(x in password for x in numbers):
        has_nums = True
    if any(x in password for x in lower_case):
        has_lower = True
    if any(x in password for x in upper_case):
        has_upper = True
    if any(x in password for x in special_characters):
        has_special_chars = True
    if len(password) >= 6:
        long_enough = True
    for x in [has_nums, has_lower, has_upper, has_special_chars]:
        if x == False:
            needed += 1
    
    if not long_enough and len(password) + needed < 6:
        needed += 6 - (len(password) + needed)
    
    return needed

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
