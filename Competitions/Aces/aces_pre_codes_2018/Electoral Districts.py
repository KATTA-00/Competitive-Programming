def bin_search(s, i, p):
    l = i
    r = len(s)
    
    while l < r:
        x = (l + r) // 2
        if (s[x] - s[i]) <= p:
            l = x + 1
        elif (s[x] - s[i]) > p:
            r = x

    return (l + r) / 2


n, p = map(int, input().strip().split())

a = [int(x) for x in input().split()]

s = [0 for i in range(n + 1)] #prefix sum array

for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i - 1]

ans = 0
for i in range(n + 1):
    a = bin_search(s, i, p)
    ans += (n - a + 1)

print (int(ans))