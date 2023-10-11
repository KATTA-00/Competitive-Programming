n = int(input())
grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

max_sum = [[0 for j in range(n)] for i in range(n)]
max_sum[0][0] = grid[0][0]

# Initialize first row and first column
for i in range(1, n):
    max_sum[i][0] = max_sum[i-1][0] + grid[i][0]
    max_sum[0][i] = max_sum[0][i-1] + grid[0][i]

# Calculate maximum sum for each square
for i in range(1, n):
    for j in range(1, n):
        max_sum[i][j] = max(max_sum[i-1][j], max_sum[i][j-1]) + grid[i][j]

print(max_sum[n-1][n-1])

# Print path
path = []
i = n - 1
j = n - 1
while i > 0 or j > 0:
    path.append((i, j))
    if i == 0:
        j -= 1
    elif j == 0:
        i -= 1
    elif max_sum[i-1][j] > max_sum[i][j-1]:
        i -= 1
    else:
        j -= 1
path.append((0, 0))
path.reverse()
for i in path:
    print(i, end=" ")
print()

