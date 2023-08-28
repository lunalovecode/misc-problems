#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    string = [*s]
    rev = [*s]
    rev.reverse()
    prev = string[0]
    diff_list_str = []
    for st in string[1:]:
        diff_list_str.append(abs(ord(prev) - ord(st)))
        prev = st
    
    prev = rev[0]
    diff_list_rev = []
    for r in rev[1:]:
        diff_list_rev.append(abs(ord(prev) - ord(r)))
        prev = r
    
    return "Funny" if diff_list_str == diff_list_rev else "Not Funny"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
