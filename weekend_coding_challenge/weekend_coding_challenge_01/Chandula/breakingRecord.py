import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    mnC, mxC = 0, 0    
    min, max = scores[0], scores[0]
    
    for i in range(1, len(scores)):
        score = scores[i]
        if score > max: 
            max = score
            mxC += 1
        elif score < min:
            mnC += 1
            min = score
    return (mnC, mxC)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
