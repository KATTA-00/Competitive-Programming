n, m = map(int, input().strip().split(" "))

grid = []
water = [[1] * m for x in range(n)]
visited = [[False] * m for x in range(n)]
topElement = []

for i in range(n):
        inp = list(map(int, input().strip().split(" ")))
        for j in range(m):
                topElement.append((inp[j], i, j))
        grid.append(inp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m

topElement.sort()
q = []
maximum = topElement[-1][0]
for top in topElement:
        # if maximum == top[0]:
        #         q.append((top[1], top[2]))
        q.append((top[1], top[2]))

while q:
    x, y = q.pop()

    visited[x][y] = True
    can = []

    flag = False
    for i in range(4):
        x_ = dx[i] + x
        y_ = dy[i] + y

        # print(x_, y_)
            
        if is_valid(x_, y_) and grid[x_][y_] < grid[x][y]:
            can.append((x_, y_))
            flag = True

    # print(can)
    if flag:
        d = len(can)
        flow = water[x][y]/d
        water[x][y] = 0
        for i in can:
                water[i[0]][i[1]] += flow
                q.append((i[0], i[1]))

m = -1
for i in water:
    #   print(i)
    m = max(m, max(i))

print( f'{m:.6f}')







