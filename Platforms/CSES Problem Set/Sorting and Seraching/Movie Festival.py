n = int(input())

times = []

for _ in range(n):
    x, y = map(int, input().strip().split(" "))

    times.append((x, y))

times.sort()

adj = []

for i in range(n):
    temp = []
    adj.append(temp)


for i in range(n-1):
    for j in range(i+1, n):
        if times[i][1] <= times[j][0]:
            adj[i].append(j)
            # adj[j].append(i)


def dfs(n):
    global visited, count
    
    if n in visited:
        return
    
    count += 1
    visited.append(n)

    for i in adj[n]:
        if i not in visited:
            dfs(i)


m = -1
for i in range(n):
    visited = []
    count = 0

    dfs(i)

    if count > m:
        m = count

print(m)

