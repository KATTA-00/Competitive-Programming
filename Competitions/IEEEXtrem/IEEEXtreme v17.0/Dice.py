# Logic : Correct
# Couldn't get full marks because of memory limit exceeded

def countWays(n, k):
    dp = [[0] * (k+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            for x in range(1, 7):
                if i >= x:
                    dp[i][j] += dp[i-x][j-1]
                    dp[i][j] %= 998244353
    total = 0
    for t in range(1, k+1):
        total += dp[n][t] * pow(6, -t, 998244353)
        total %= 998244353
    return (total * pow(k, -1, 998244353)) % 998244353

n, k = map(int, input().split())
result = countWays(n, k)
print(result)








