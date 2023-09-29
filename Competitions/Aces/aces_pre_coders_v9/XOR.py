n = int(input())

for i in range(n):
    a = int(input())
    arr = list(map(int,input().strip().split()))

    if a == 1:
        print(arr[0])
    elif a%2 != 0:
        ans = 0
        for val in range(0,a,2):
            ans = ans^arr[val]
        print(ans)
    else:
        print(0)