n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
leftArr = []
rightArr = []
for i in range(1, len(arr)):
    if arr[0] > arr[i]:
        leftArr.append(arr[i])
    else:
        rightArr.append(arr[i])
leftArr.append(arr[0])
print(leftArr + rightArr) 