def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def dfs(graph, values, v, l, r, dist, parent):
    if dist < r - l:
        values[v] = phi(l + dist)
    dist += 1
    for neighbor in graph[v]:
        if neighbor != parent:
            if dist < r - l:
                values[neighbor] = phi(l + dist)
                dfs(graph, values, neighbor, l, r, dist, v)

def dfsParent(n = 1, p = 0):
    global parent
    parent[n] = p

    for neighbor in graph[n]:
        if neighbor != p:
            dfsParent(neighbor, n)

n = int(input())
graph = {i: [] for i in range(n + 1)}
values = [0] * (n + 1)
parent = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfsParent()

for neighbor in graph[1]:
    dfs(graph, values, neighbor, 0, 1, 1, 1)

q = int(input())
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        v, l, r = query[1], query[2], query[3]
        dfs(graph, values, v, l, r, 0, parent[v])
    elif query[0] == 2:
        v = query[1]
        print(values[v])
