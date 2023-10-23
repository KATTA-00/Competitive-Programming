class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def isIntersecting(current,setCircle,R):
    x1,y1 = current[0],current[1]
    x2,y2 = setCircle[0],setCircle[1]
    
    if (x1-x2)**2+ (y1-y2)**2 <=4*R**2:
        return True
    
    else: return False



t, row, col = list(map(int, input().strip().split()))
for _ in range(t):
    N, r = list(map(int, input().strip().split()))
    

    xCoor = [int(i) for i in input().strip().split()]
    yCoor = [int(i) for i in input().strip().split()]
    
    circles = []
    for i in range(N):
        circles.append((xCoor[i],yCoor[i]))

    circles.sort()

    pointMap = {}
    for i in range(N):
        pointMap[circles[i]] = i

    dsu = DSU(N)

    count = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if (isIntersecting(circles[i], circles[j],r)):
                dsu.union(pointMap[circles[i]], pointMap[circles[j]])

    cicurSet = [{x} for x in circles]

    for i in circles:
        par = dsu.find(pointMap[i])
        cicurSet[par].add(i)
            
    for group in cicurSet:
        xmin = min([x - r for (x,y) in group])
        xmax = max([x + r for (x,y) in group])
        # print(xmin,xmax)
        if xmin <= 0 and xmax >= row:
            print("CAN'T")
            break
    else:
        print("CAN")
    
    