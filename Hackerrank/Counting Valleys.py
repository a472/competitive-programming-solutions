#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    f=0
    g=0
    count=0
    for i in s:
        if i=='U':
            f=f+1
        elif i=='D':
            f=f-1

        if g==f and i=='U':
            count=count+1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
