# def longest_increasing_subsequence(arr):
#     n = len(arr)
#     dp = [1] * n
#     for i in range(1, n):
#         for j in range(i):
#             if arr[i] > arr[j]:
#                 dp[i] = max(dp[i], dp[j] + 1)
#     return max(dp)

# arr = [10, 22, 9, 33, 21, 50, 41, 60]
# print(longest_increasing_subsequence(arr))

# The following code solves the problem in O(n^2) time using dynamic programming.

# print the longest increasing subsequence
def print_lis(arr, dp):
    n = len(arr)
    i = dp.index(max(dp))
    lis = [arr[i]]
    while i > 0:
        for j in range(i - 1, -1, -1):
            if arr[j] < arr[i] and dp[j] == dp[i] - 1:
                lis.append(arr[j])
                i = j
                break
    lis.reverse()
    return lis

arr = [10, 22, 9, 33, 21, 50, 41, 60]
dp = [1] * len(arr)
for i in range(1, len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(print_lis(arr, dp))
print(max(dp))


