n = int(input())

arr = [1.0,1.0,2.0,4.0]
sum = 0.0

for i in range (2,n):
    arr.append(arr[i]/arr[i-2])

for j in range(n):
    sum += arr[j]

print(sum)