from collections import deque

MOD = 10**9 + 9
MAXN = 10**6 + 5

def add_edge(u, v):
    graph[u].append(v)
    graph[v].append(u)

def bfs(s, t):
    queue = deque([(s, 0)])
    dist[s] = 0
    ways[s] = 1
    while queue:
        u, d = queue.popleft()
        if u == t: return d
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = d + 1
                ways[v] = ways[u]
                queue.append((v, d + 1))
            elif dist[v] == d + 1:
                ways[v] += ways[u]
                ways[v] %= MOD
    return -1

def solve():
    n, t, h0, a, b, q = input().split()
    n = int(n)
    t = int(t)
    h0 = int(h0)
    a = int(a)
    b = int(b)
    q = int(q)

    MAXV = 10**n
    for i in range(MAXN):
        graph[i].clear()
        
    for i in range(MAXV):
        dist[i] = -1
        ways[i] = 0

    h = [0]*MAXN
    h[0] = h0 % MAXV
    add_edge(0, h[0])
    
    for i in range(1, MAXN):
        h[i] = (a * h[i-1] + b) % q
        h[i] %= MAXV
        
        add_edge(h[i-1], h[i])
        
        if h[i-1] == t or h[i] == t: break

    print(h)

    d = bfs(0, t)
    
    if d == -1:
        print(-1)
    else:
        print(d, ways[t])

c = int(input())
graph = [[] for _ in range(MAXN)]
dist = [-1]*MAXN
ways = [0]*MAXN

for _ in range(c):
    solve()
