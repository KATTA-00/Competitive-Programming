n, t = list(map(int, input().strip().split(" ")))

arr = list(map(int, input().strip().split(" ")))


for _ in range(t):
    temp = arr.copy()
    for i in range(n-1):
        if temp[i] == 0 and temp[i+1] == 1:
            arr[i] = 1
            arr[i+1] = 0
            
print(" ".join([str(x) for x in arr]))