num = int(input())

arr = [int(x) for x in input().strip().split(' ')]

rm = [int(x) for x in input().strip().split(' ')]

for i in rm:
    print(arr[i-1], end=" ")
    del arr[i-1]