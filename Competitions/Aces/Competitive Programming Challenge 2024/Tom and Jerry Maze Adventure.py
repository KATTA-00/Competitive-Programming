m, n = map(int, input().strip().split(" "))

grid = []
visited = [[False for i in range(n)] for j in range(m)]
count = [[99999 for i in range(n)] for j in range(m)]
x, y = 0,0
l, r = 0, 0

for i in range(m):
    temp = list(input().strip())
    grid.append(temp)

    for j in temp:
        if j == "T":
            x, y = i, temp.index(j)


def is_valid(x, y):
    return x >= 0 and x < m and y >= 0 and y < n and grid[x][y] != "#" and not visited[x][y]

def bfs(x, y):
    global l, r
    queue = [(x, y)]
    visited[x][y] = True
    count[x][y] = 0

    while queue:
        x, y = queue.pop(0)

        if grid[x][y] == "J":
            l,r = x, y
            return True
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                
                if (i == 0 or j == 0) and is_valid(x + i, y + j):
                    queue.append((x + i, y + j))
                    visited[x + i][y + j] = True

                    if count[x + i][y + j] > count[x][y] + 1:
                        count[x + i][y + j] = count[x][y] + 1

    return False


if bfs(x, y):
    print("YES")
    print(count[l][r])
else:
    print("IMPOSSIBLE")