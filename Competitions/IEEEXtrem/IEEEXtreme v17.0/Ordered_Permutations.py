# Logic : Correct
# Couldn't get full marks because of memory limit exceeded

def countPermutations(N, R):
    MOD = 10**9 + 7
    dp = [[0]*(N+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        s = [0]*(N+2)
        for j in range(i+1):
            s[j+1] = (s[j] + dp[i-1][j]) % MOD
        for j in range(i+1):
                dp[i][j] = (dp[i][j] + (s[j] if R[i-1:i] == "<" 
                                        else s[i]-s[j])) % MOD
    return sum(dp[N-1]) % MOD



N = int(input())
R = input().strip()
result = countPermutations(N, R)
print(result)
