#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    on_horizontal_line = True
    on_vertical_line = True
    xy = input().split()
    prev_x = int(xy[0])
    prev_y = int(xy[1])
    for n_itr in range(n - 1):
        xy = input().split()

        x = int(xy[0])

        y = int(xy[1])
        
        if x != prev_x:
            on_horizontal_line = False
        
        if y != prev_y:
            on_vertical_line = False
        
        prev_x = x
        prev_y = y
    
    print("YES" if any([on_horizontal_line, on_vertical_line]) else "NO")