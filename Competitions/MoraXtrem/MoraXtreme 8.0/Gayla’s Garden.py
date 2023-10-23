def num_of_showers(x, k):
    ans = 0
    x.sort()
    i = 0
    while i < len(x):
        reach = x[i] + k
        j = i + 1
        while j < len(x) and x[j] <= reach:
            j += 1
        i = j - 1
        reach = x[i] + k
        j = i + 1
        while j < len(x) and x[j] <= reach:
            j += 1
        i = j
        ans += 1
    return ans




n, k = map(int, input().rstrip().split())
x = list(map(int, input().rstrip().split()))

print(num_of_showers(x, k))