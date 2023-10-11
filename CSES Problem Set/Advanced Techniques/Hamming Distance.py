N, M = map(int, input().split())

arr = []
for _ in range(N):
    s = input().strip()
    arr.append(int(s, 2))

m = M
for i in range(N):
    for j in range(i+1, N):
        s = bin(arr[i]^arr[j])[2:].count("1")
        if m > s:
            m=s

print(m)