#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def solve(a):
    numofones = a.count(1)
    numoftwos = a.count(2)
    
    total  = numofones*(numofones-1) + (len(a) - numofones) * numofones + int(numoftwos * (numoftwos-1)/2)
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a_count = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = solve(a)

        fptr.write(str(result) + '\n')

    fptr.close()
