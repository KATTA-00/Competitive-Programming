#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    dp = [1000000]*len(c)
    
    if c[0]==0:
        dp[0]=0
        
    if c[1] == 0:
        dp[1] =1
    
    for i in range(2,len(c)):
        if c[i]!=1:
                
            dp[i] = min(dp[i-2], dp[i-1])+1
    # print(dp)
    return dp[len(c)-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
