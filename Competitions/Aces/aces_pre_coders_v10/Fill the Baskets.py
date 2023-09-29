n = int(input())

m = int(input())

ballValues = [int(i) for i in input().strip().split()]

c = int(input())
freeBaskets = n

ballValues.sort(reverse=True)

while len(ballValues)!=0:
    basketSum = ballValues.pop(0)
    flag = True
    i=0
    while(i<len(ballValues)):
        if(basketSum==c):
            flag = False
            freeBaskets-=1
            break
      
        elif(basketSum+ballValues[i]<=c):
            # print(basketSum)
            basketSum+=ballValues.pop(i)
            # print('after',basketSum)
      
        else:
            i+=1

    if(flag==True):
        freeBaskets-=1
        
print(freeBaskets*10)    
