num = int(input())

arr = list(map(int, input().strip().split(" ")))

arr.sort()

for i in range(1, num):
    
    if i!=arr[i-1]:
        print(i)
        break
else:
    print(num)