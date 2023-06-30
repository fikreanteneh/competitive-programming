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

def countSwaps(heights):
    n = len(heights)
    ans = 0
    for i in range(n - 1,0,-1):
        for j in range(i):
            if heights[j] > heights[j+1]:
                heights[j], heights[j+1] = heights[j+1], heights[j]
                ans+=1
    print("Array is sorted in", ans, "swaps." )
    print("First Element:",heights[0])
    print("Last Element:",heights[-1])
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
