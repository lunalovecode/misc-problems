#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
    # The most conditions I have ever written
    
    if m == 0:
        return f"{nums[h - 1]} o' clock"
    elif m == 15:
        return f"quarter past {nums[h - 1]}"
    elif m == 30:
        return f"half past {nums[h - 1]}"
    elif m == 45:
        return f"quarter to {nums[h]}"
    elif 20 < m < 30:
        return f"twenty {nums[m - 21]} minutes past {nums[h - 1]}"
    elif 20 < (59 - m) < 30:
        return f"twenty {nums[(59 - m) - 20]} minutes to {nums[h]}"
    elif 1 < (59 - m) < 20:
        return f"{nums[(59 - m)]} minutes to {nums[h]}"
    elif m == 1:
        return f"one minute past {nums[h - 1]}"
    elif m == 59:
        return f"one minute to {nums[h]}"
    elif m <= 20:
        return f"{nums[m - 1]} minutes past {nums[h - 1]}"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
