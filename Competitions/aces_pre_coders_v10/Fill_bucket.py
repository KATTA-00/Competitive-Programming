n = int(input())

m = int(input())

arr = [int(x) for x in input().strip().split(" ")]

t = int(input())

arr.sort(reverse=True)

r = len(arr) - 1
l = 0

count = 0
while True:

    # if arr[l] >= t:
    #         count+=1
    #         l-=1
    #         continue
    
    flag = False
    for i in range(1, l):

        if (sum(arr[:i]) + arr[l] > t):

            if (i == 1):
                count+=1
                l-=1
                break

            

            arr = arr[:i-1]    

    arr = 

