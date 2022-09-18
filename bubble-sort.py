#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    c = 0
    if len(a) == 1:
        return a
    for i in range(len(a) - 1,0,-1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                c += 1
    print("Array is sorted in", c, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])
    return a

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
