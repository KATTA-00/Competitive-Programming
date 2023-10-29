N, x = map(int, input().split())
t = list(map(int, input().split()))
t.sort()

if N == 1:
    print(1 if x == t[0] else 0)
else:
    freq = {}
    for i in range(1 << (N // 2 - 1)):
        sum_val = 0
        for j in range(N // 2 - 1):
            if i & (1 << j):
                sum_val += t[j]
        freq[sum_val] = freq.get(sum_val, 0) + 1

    cnt = 0
    for i in range(1 << ((N + 1) // 2 + 1)):
        sum_val = 0
        for j in range((N + 1) // 2 + 1):
            if i & (1 << j):
                sum_val += t[N // 2 - 1 + j]
        cnt += freq.get(x - sum_val, 0)

    print(cnt)
