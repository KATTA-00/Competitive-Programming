n, m = [int(x) for x in input().strip().split(" ")]

arr = [int(x) for x in input().strip().split(" ")]

dff = [0] * (n+1)

for i in range(1, n+1):
    dff[i] = dff[i-1] + arr[i-1]

for _ in range(m):
    a, b = [int(x) for x in input().strip().split(" ")]

    print(dff[b]-dff[a-1])