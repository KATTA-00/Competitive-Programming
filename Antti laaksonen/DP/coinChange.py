# we are given a set of coin values, and
# our task is to construct a sum of money using as few coins as possible

# The problem is known to be NP-complete, meaning that the only known solution
# to the problem is to evaluate all possible subsets of the coins.
# Therefore, the problem has no known polynomial-time algorithm, but it is
# believed that the problem can not be solved in polynomial time.
# However, this does not mean that the problem could not be solved efficiently
# in practice. In fact, the problem can be solved efficiently using dynamic programming.


# The idea is to go through the coins and for each coin consider all sums of
# money that can be constructed using the coin. For each sum, we can then
# update the minimum number of coins needed to construct the sum.

# The following code solves the problem in O(n·x) time, where n is the number
# of coins and x is the desired sum of money. The code uses a one-dimensional
# array t, where t[y] is the minimum number of coins needed to construct the
# sum y. The array is filled using a loop, where the value of t[y] is updated
# using the values of t[y−c] for all coins c.

# The code also prints the coins that are used to construct the sum. This is
# done by storing to the array k the last coin that was added to the sum y.
# After the array t has been filled, we can go through the coins that were
# used by following the chain k[y]→k[k[y]]→k[k[k[y]]]→… until we reach the
# value 0.

# The code assumes that the coin values are integers. If the coin values are
# real numbers, the code can be modified to use integers by multiplying all
# values by 100.


def coinChange(coins, x):
    n = len(coins)
    t = [0] * (x + 1)
    k = [0] * (x + 1)
    for y in range(1, x + 1):
        t[y] = 1e9
        for i in range(n):
            if y >= coins[i] and t[y - coins[i]] + 1 < t[y]:
                t[y] = t[y - coins[i]] + 1
                k[y] = i
    if t[x] == 1e9:
        return -1
    else:
        ans = []
        while x > 0:
            ans.append(coins[k[x]])
            x -= coins[k[x]]
        return ans
    
coins = [1, 3, 5, 7, 11, 13, 17, 19, 23]
x = 50

print(coinChange(coins, x))

# if they can use each coin only once, the problem can be solved in O(n·x) time
# using dynamic programming. The idea is to go through the coins and for each
# coin consider all sums of money that can be constructed using the coin.
# For each sum, we can then update the minimum number of coins needed to
# construct the sum.

# The following code solves the problem in O(n·x) time, where n is the number
# of coins and x is the desired sum of money. The code uses a two-dimensional
# array t, where t[y][z] is the minimum number of coins needed to construct the
# sum y using the first z coins. The array is filled using a loop, where the
# value of t[y][z] is updated using the values of t[y−c][z−1] for all coins c.

# The code also prints the coins that are used to construct the sum. This is
# done by storing to the array k the last coin that was added to the sum y.
# After the array t has been filled, we can go through the coins that were
# used by following the chain k[y][z]→k[k[y][z]][z−1]→k[k[k[y][z]][z−1]][z−2]→… until we reach the value 0.


def coinChange(coins, x):
    n = len(coins)
    t = [[0] * (n + 1) for _ in range(x + 1)]
    k = [[0] * (n + 1) for _ in range(x + 1)]
    for y in range(1, x + 1):
        t[y][0] = 1e9
        for z in range(1, n + 1):
            t[y][z] = t[y][z - 1]
            k[y][z] = k[y][z - 1]
            if y >= coins[z - 1] and t[y - coins[z - 1]][z - 1] + 1 < t[y][z]:
                t[y][z] = t[y - coins[z - 1]][z - 1] + 1
                k[y][z] = z
    if t[x][n] == 1e9:
        return -1
    else:
        ans = []
        while x > 0:
            ans.append(coins[k[x][n] - 1])
            x -= coins[k[x][n] - 1]
            n -= 1
        return ans
    
print(coinChange(coins, x))