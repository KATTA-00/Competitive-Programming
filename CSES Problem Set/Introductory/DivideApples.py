def min_diff(arr, n, sum1, sum2):
    if n == 0:
        return abs(sum1 - sum2)
    
    return min(
        min_diff(arr, n - 1, sum1 + arr[n - 1], sum2),
        min_diff(arr, n - 1, sum1, sum2 + arr[n - 1])
    )


n = int(input())
arr = list(map(int, input().split()))
print(min_diff(arr, n, 0, 0))
