from sys import maxsize

def maxSubArraySum(a, size):
    max_so_far = -maxsize - 1
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here += a[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    if max_so_far < 0:
        return 0
    return max_so_far

n, m = map(int, input().strip().split())

arr = list(map(int, input().strip().split()))

for _ in range(m):
    a, b = map(int, input().strip().split())
    a -= 1
    arr[a] = b
    print(maxSubArraySum(arr, n))
