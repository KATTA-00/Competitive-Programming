mod = 10**9 + 7

grid_size = int(input())
paths = [[0] * (grid_size + 1) for _ in range(grid_size + 1)]
paths[0][0] = 1

for i in range(grid_size):
    row = input()

    for j in range(grid_size):
        if row[j] != '*':
            if i > 0:
                paths[i][j] += paths[i - 1][j]
                paths[i][j] %= mod
            if j > 0:
                paths[i][j] += paths[i][j - 1]
                paths[i][j] %= mod
        else:
            paths[i][j] = 0

print(paths[grid_size - 1][grid_size - 1] % mod if grid_size > 0 else -1)


