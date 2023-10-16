n=int(input().strip())

arr=list(map(int,input().split()))

Count=0

for i in range(1,len(arr)):
    if arr[i-1]>arr[i]:
        Count+=arr[i-1]-arr[i]
        arr[i]=arr[i-1]

print(Count)