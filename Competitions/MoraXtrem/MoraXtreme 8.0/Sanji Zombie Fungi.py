n = int(input())
cellCount = [int(i) for i in input().strip().split()]
cellPoss = [int(i) for i in input().strip().split()]
m = int(input())
fungiCells = [int(i) for i in input().strip().split()]
fungiRad = [int(i) for i in input().strip().split()]
numberOfLayers = [0]*n

for j in range(n):
    for i in range(m):
        if fungiCells[i]-fungiRad[i]<=cellPoss[j]<=fungiCells[i]+fungiRad[i]:
            numberOfLayers[j]+=1
# print(numberOfLayers)
goodCells = 0
for i,number in enumerate(numberOfLayers):
    if number ==0 or number==1:
        goodCells+=cellCount[i]

print(goodCells)
