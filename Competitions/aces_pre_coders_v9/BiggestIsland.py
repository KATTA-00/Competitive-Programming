def is_valid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def dfs(grid, x, y, n, m):
    if not is_valid(x, y, n, m) or grid[x][y] == 0:
        return 0

    grid[x][y] = 0  # Mark the cell as visited
    area = 1  # Initialize area for this island

    # 8-adjacent directions
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        area += dfs(grid, new_x, new_y, n, m)

    return area

def find_largest_island(grid):
    n = len(grid)
    m = len(grid[0])
    max_area = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                island_area = dfs(grid, i, j, n, m)
                max_area = max(max_area, island_area)

    return max_area

# Input parsing
n = int(input())
m = int(input())

grid = []
for _ in range(n):
    row = list(map(int, input().strip().split()))
    grid.append(row)

# Find and output the area of the largest island
largest_island_area = find_largest_island(grid)
print(largest_island_area)