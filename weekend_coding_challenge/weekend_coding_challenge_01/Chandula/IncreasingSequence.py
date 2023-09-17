def winnerIs(arr,k):
    player = ["First","Second"]

    if k==1:
        print(player[0])
    else:
        setArr = set(arr)
        if len(setArr) != k:
            print(player[(k-1)%2])
        else:
            print(player[0])

n = int(input().strip())

for j in range(n):
    k = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    winnerIs(arr,k)