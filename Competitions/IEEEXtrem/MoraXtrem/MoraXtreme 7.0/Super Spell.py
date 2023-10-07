t = int(input())

for _ in range(t):
    n = int(input())
    a = []
    for i in range(n):
        arr = list(input())
        arr.sort()
        a.append(arr[0])
        
    a.sort()
    print("".join(a))
