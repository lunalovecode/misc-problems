#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    new_str = []
    for char in s:
        if char.isalpha():
            if char.isupper() and ord(char) + (k % 26) > ord("Z"):
                new_str.append(chr(ord("A") + (ord(char) + k % 26) - ord("Z") - 1))
            elif char.islower() and ord(char) + (k % 26) > ord("z"):
                new_str.append(chr(ord("a") + (ord(char) + k % 26) - ord("z") - 1))
            else:
                new_str.append(chr(ord(char) + (k % 26)))
        else:
            new_str.append(char)
    return "".join(new_str)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
