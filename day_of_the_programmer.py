#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    leap = False
    new_date = ["09", str(year)]
    
    if year < 1918:
        if year % 4 == 0:
            leap = True
    elif year > 1918:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            leap = True
    
    if leap == True and year != 1918:
        new_date.insert(0, "12")
    elif leap == False and year != 1918:
        new_date.insert(0, "13")
    else:
        new_date.insert(0, "26")
    
    return ".".join(new_date)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
