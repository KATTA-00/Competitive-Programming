# the possible sums for weights [1, 3, 3, 5]

weights = [1, 3, 3, 5]
n = len(weights)
total_sum = sum(weights)

# Initialize dp array
dp = [[False for j in range(total_sum+1)] for i in range(n+1)]
dp[0][0] = True

# Fill dp array
for i in range(1, n+1):
    for j in range(total_sum+1):
        if dp[i-1][j]:
            dp[i][j] = True
        if j >= weights[i-1] and dp[i-1][j-weights[i-1]]:
            dp[i][j] = True

# Print possible sums
for j in range(total_sum+1):
    if dp[n][j]:
        print(j)
#----------------------------------------------------------------------------------------------

# a situation where objects have
# weights and values and we have to find a maximum value subset whose weight does
# not exceed a given limit
# Example input values
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
max_weight = 7

# Initialize the dynamic programming table
n = len(weights)
dp = [[0 for j in range(max_weight+1)] for i in range(n+1)]

# Fill the dynamic programming table
for i in range(1, n+1):
    for j in range(1, max_weight+1):
        if weights[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + values[i-1])

# Print the maximum value that can be obtained
print(dp[n][max_weight])

#----------------------------------------------------------------------------------------------
# Example input values
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
max_weight = 8

# Initialize the dynamic programming table and the item tracker
n = len(weights)
dp = [[0 for j in range(max_weight+1)] for i in range(n+1)]
items = [[[] for j in range(max_weight+1)] for i in range(n+1)]

# Fill the dynamic programming table and the item tracker
for i in range(1, n+1):
    for j in range(1, max_weight+1):
        if weights[i-1] > j:
            dp[i][j] = dp[i-1][j]
            items[i][j] = items[i-1][j]
        else:
            if dp[i-1][j] > dp[i-1][j-weights[i-1]] + values[i-1]:
                dp[i][j] = dp[i-1][j]
                items[i][j] = items[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-weights[i-1]] + values[i-1]
                items[i][j] = items[i-1][j-weights[i-1]] + [i]

# Print the maximum value that can be obtained and the corresponding subset of items
print("Maximum value:", dp[n][max_weight])
print("Subset of items:", items[n][max_weight])