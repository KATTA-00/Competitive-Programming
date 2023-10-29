#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'berthType' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def berthType(n):
    switcher = {
        0: "SUB",
        1: "LB",
        2: "MB",
        3: "UB",
        4: "LB",
        5: "MB",
        6: "UB",
        7: "SLB"
    }
    return switcher.get(n, "nothing")
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = berthType(n%8)

    fptr.write(result + '\n')

    fptr.close()
