t = int(input())

def dfs(n):
    global grid, colour, visited
    
    visited[n] = True
    
    for i in grid[n]:
        
        if not visited[i]:
            colour[i] = 1 if colour[n] == 2 else 2
            if dfs(i) == 1:
                return 1
        else:
            if colour[n] == colour[i]:
                print("YES")
                return 1
        
    return 0

for _ in range(t):
    n, m = [int(x) for x in input().strip().split(" ")]
    
    grid = [set() for x in range(n)]
    colour = [0 for x in range(n)]
    visited = [False for x in range(n)]
    
    for i in range(m):
        a, b = [int(x) for x in input().strip().split(" ")]
        grid[a-1].add(b-1)
        
        
    colour[0] = 1
    if dfs(0) == 0:
        print("NO")
