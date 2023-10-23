def strings_steps(a, b, s):
    N = len(s)
    cost = [0]*N
    cost[0] = a
    index = 1
    for i in range(1,N):
        if s[index:i+1] not in s[:index] or index == -1:
            index = LongestOccurence(s[:i+1], i)
        if index==-1:
            cost[i] = cost[i-1] + a
        else:
            cost[i] = min(cost[i-1]+a, cost[index-1]+b)
    return cost[-1]

def LongestOccurence(s, index):
    isChanged = False
    while s[index:] in s[:index]:
        index -= 1
        isChanged = True
    return -1 if not isChanged else index + 1


T = int(input())
for _ in range(T):
    l, a, b = map(int, input().split())
    s = input().strip()
    result = strings_steps(a, b, s)
    print(result)
