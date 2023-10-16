import math

t = int(input())
dp = [[0]*t for _ in range(t)]
points = []
points.append([int(i) for i in input().strip().split()])

totalLength = 0
for i in range(1,t):
    points.append([int(i) for i in input().strip().split()])
    totalLength+= math.sqrt((points[i][0]-points[i-1][0])**2+(points[i][1]-points[i-1][1])**2)

totalLength+= math.sqrt((points[t-1][0]-points[0][0])**2+(points[t-1][1]-points[0][1])**2)
print(round(totalLength,2))