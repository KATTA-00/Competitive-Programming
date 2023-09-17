n = int(input().strip())

arr = list(map(int, input().rstrip().split()))


sum_even=0
for k in range(0,len(arr),2):
    sum_even+=arr[k]
sum_odd=0
for j in range(1,len(arr),2):
    sum_odd+=arr[j]
if sum_even>sum_odd:
    print(2*sum_odd)
else :
    print(2*sum_even)