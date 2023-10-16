t = int(input())

def compute_total(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    diff_dict = {}
    total_sum = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) not in diff_dict:
                diff = abs(arr[i] - arr[j])
                diff_dict[(i, j)] = diff
                diff_dict[(j, i)] = diff
            else:
                diff = diff_dict[(i, j)]

            dp[i][j] = diff
            dp[j][i] = diff
            total_sum[i] += diff
            total_sum[j] += diff

    for i in range(n):
        total_sum[i] += n

    return dp, total_sum

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().strip().split()]

    dp_result, total_sum = compute_total(arr)

    for i in range(n):
        print(total_sum[i], end=" ")
    print()
