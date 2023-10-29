from typing import List
import bisect
X = [0] * 2000005
Y = [0] * 2000005
 
def calcsubarray(a, x, n, c):
    for i in range((1 << n)):
        s = 0
        for j in range(n):
            if (i & (1 << j)):
                s += a[j + c]
        x[i] = s
 
# Returns the maximum possible sum less or equal to S
def solveSubsetSum(a, n, S) :
    global Y
     
    calcsubarray(a, X, n // 2, 0)
    calcsubarray(a, Y, n - n // 2, n // 2)
    size_X = 1 << (n // 2)
    size_Y = 1 << (n - n // 2)

    YY = Y[:size_Y]
    YY.sort()
    Y = YY
 
    maxx = 0

    for i in range(size_X):
 
        if (X[i] <= S):
 
            p = bisect.bisect_left(Y, S - X[i])

            if (p == size_Y or (p < size_Y and Y[p] != (S - X[i]))):
                p -= 1
            if ((Y[p] + X[i]) == S):
                maxx +=1
    return maxx
 
# Driver code
if __name__ == "__main__":
 
    n, s = list(map(int, input().strip().split(' ')))
    arr = list(map(int, input().strip().split(' ')))

    print("Largest value smaller than or equal to given sum is {}".format(
		solveSubsetSum(arr, n, s)))