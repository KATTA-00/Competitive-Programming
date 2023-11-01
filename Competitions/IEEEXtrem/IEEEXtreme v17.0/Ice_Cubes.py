# coudn't get not full marks but got above 70% 

t = int(input())

def calculate_max_ice_cubes(grid, max_bad_coffees, bad_coffee_threshold):
    num_rows = len(grid)
    num_cols = len(grid[0])
    dp = {}  # dynamic programming table

    def dfs(row, col, consecutive_bad_coffees):
        if consecutive_bad_coffees <= 0:
            dp[(row, col, consecutive_bad_coffees)] = float('-inf')
            return dp[(row, col, consecutive_bad_coffees)]
        if row == num_rows - 1 and col == num_cols - 1:
            if grid[row][col] < bad_coffee_threshold:
                if consecutive_bad_coffees <= 1:
                    dp[(row, col, consecutive_bad_coffees)] = float('-inf')
                    return dp[(row, col, consecutive_bad_coffees)]
            dp[(row, col, consecutive_bad_coffees)] = grid[row][col]
            return dp[(row, col, consecutive_bad_coffees)]

        if (row, col, consecutive_bad_coffees) in dp:
            return dp[(row, col, consecutive_bad_coffees)]

        directions = [(0, 1), (1, 0)]
        max_ice_cubes = float('-inf')
        for dx, dy in directions:
            if row + dx >= num_rows or col + dy >= num_cols:
                continue
            if grid[row][col] < bad_coffee_threshold:
                max_ice_cubes = max(max_ice_cubes,
                                    grid[row][col] + dfs(row + dx,
                                                          col + dy,
                                                          consecutive_bad_coffees - 1))
            else:
                max_ice_cubes = max(max_ice_cubes,
                                    grid[row][col] + dfs(row + dx,
                                                          col + dy,
                                                          max_bad_coffees))
        dp[(row, col, consecutive_bad_coffees)] = max_ice_cubes
        return dp[(row, col, consecutive_bad_coffees)]

    dfs(0, 0, max_bad_coffees)
    return dp[(0, 0, max_bad_coffees)] if dp[(0, 0, max_bad_coffees)] != float('-inf') else "IMPOSSIBLE"

for test_case in range(1, t + 1):
    n_rows_cols_maxbadcoffee_badcubethreshold = list(map(int,input().split()))
    words = [list(map(int,input().split())) for _ in range(n_rows_cols_maxbadcoffee_badcubethreshold[0])]
    max_ice_cubes = calculate_max_ice_cubes(words,
                                            n_rows_cols_maxbadcoffee_badcubethreshold[2],
                                            n_rows_cols_maxbadcoffee_badcubethreshold[3])
    print(f"Case {test_case}: {max_ice_cubes}")


