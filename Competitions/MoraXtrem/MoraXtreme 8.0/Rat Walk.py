t, row, col = list(map(int, input().strip().split()))

def checkNei(x, y, x_, y_):
    global r
    dis = (x-x_)**2 + (y-y_)**2
    
    if 4 * r**2 >= dis:
        return True
    else:
        return False


def dfs(point):
    global visited, adjMap, r

    if point[0] + r >= row:
        return 0
    
    visited[pointMap[point]] = True

    for p in adjMap[point]:

        if not visited[pointMap[p]]:
            if dfs(p) == 0:
                return 0
            else:
                return 1
            
    return 1
            

for _ in range(t):
    # print()
    n, r = list(map(int, input().strip().split()))
    
    visited = [False for x in range(n)]
    
    arr_x = list(map(int, input().strip().split()))
    arr_y = list(map(int, input().strip().split()))
    
    points = [(arr_x[i], arr_y[i]) for i in range(n)]
    adjMap = {}
    pointMap = {}
    
    points = sorted(points, key=lambda x: x[0])
    
    for i in range(n):
        adjMap[points[i]] = []
        pointMap[points[i]] = i
    
    for i in range(n-1):
        for j in range(i+1, n):
            if checkNei(points[i][0], points[i][1], points[j][0], points[j][1]):
                adjMap[points[i]].append(points[j])
                adjMap[points[j]].append(points[i])

    starts = []
    
    for i in points:
        if i[0] <= r:
            starts.append(i)
    
    for i in starts:
        visited = [False for x in range(n)]
        if dfs(i) == 0:
            print("CAN'T")
            break
    else:
        print("CAN")
            
    
        
    
    
    
    