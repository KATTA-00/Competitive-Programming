#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stonePiles' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
def compute_sg_fun(prev, start, rest, key, sg_fun, record):
    i = start
    while i <= rest // 2:
        if rest - i > i:
            res = prev ^ sg_fun[i] ^ sg_fun[rest - i]
            record[key][res] = True
            compute_sg_fun(prev ^ sg_fun[i], i + 1, rest - i, key, sg_fun, record)
        i += 1

    k = 0
    while record[key][k]:
        k += 1

    sg_fun[key] = k


def stonePiles(arr):
    record = [[False] * 51 for _ in range(51)]
    sg_fun = [-1] * 51
    sg_fun[0] = 0
    sg_fun[1] = 0
    sg_fun[2] = 0
    sg_fun[3] = 1

    for i in range(4, 51):
        compute_sg_fun(0, 1, i, i, sg_fun, record)
    ans=0
    for i in range(len(arr)):
        ans^=sg_fun[arr[i]]
    if ans==0:
        return "BOB"
    return "ALICE"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = stonePiles(arr)

        fptr.write(result + '\n')

    fptr.close()