#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    i = n - 2
    for i in range(i, -1, -1):
        j = i + 1
        keyM = arr[i]
        while j < n and keyM > arr[j]:
            key = arr[j]
            arr[j] = keyM
            p = list(map(str, arr ))
            print((" ".join(p)))
            arr[j-1] = key
            j+=1
    p = list(map(str, arr ))
    print((" ".join(p)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
