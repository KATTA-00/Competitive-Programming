#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    char_count = {}
    for char in b:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char, count in char_count.items():
        if char != '_' and count == 1:
            return "NO"
    
    if '_' not in char_count:
        for i in range(1, len(b) - 1):
            if b[i] != b[i - 1] and b[i] != b[i + 1]:
                return "NO"
    
    if '_' in char_count and any(count == 1 for char, count in char_count.items() if char != '_'):
        return "NO"
    
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
