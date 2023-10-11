n, s = list(map(int, input().strip().split(' ')))

arr = list(map(int, input().strip().split(' ')))

sumArr = [0 for x in range(n+1)]
sumArr[1] = arr[0]

for i in range(2, n+1):
    sumArr[i] = arr[i-1] + sumArr[i-1]

c = 0
for i in range(n):
    for j in range(i+1, n):
        ss = sumArr[j+1] - sumArr[i]
        if ss == s:
            c+=1

print(c)
