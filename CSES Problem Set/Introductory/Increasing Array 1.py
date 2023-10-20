num = int(input())

arr = list(map(int, input().strip().split(" ")))

moves = 0
for i in range(num-1):
    dff = arr[i] - arr[i+1]

    if dff > 0:
        moves+=dff
        arr[i+1] = arr[i]

print(moves)