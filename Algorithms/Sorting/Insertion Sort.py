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
    num = arr[-1]
    l=len(arr)
    if l!=1:
        ind = -2
        while -ind<=l and arr[ind]>num:
            arr[ind+1]=arr[ind]
            ind-=1
            out = list(map(str,arr))
            print(' '.join(out))
        arr[ind+1]=num
        out = list(map(str,arr))
        print(' '.join(out))
    else:
        print(num)
    return None



def insertionSort2(n,arr):
    length = len(arr)
    for i in range(1,length):
        key = arr[i]
        ind = i-1
        while ind>=0 and arr[ind]>key:
            arr[ind+1]=arr[ind]
            ind-=1
        arr[ind+1] = key
        out = list(map(str,arr))
        print(' '.join(out))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n,arr)