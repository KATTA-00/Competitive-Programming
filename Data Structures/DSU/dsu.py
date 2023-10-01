class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


def earliest_communication_times(N, M, Q, pairs, queries):
    for i in range(Q):
        dsu = DSU(N)
        a, b = queries[i]
        
        for j in range(M):
            t, x, y = pairs[j]
            dsu.union(x-1, y-1)
            
            if dsu.find(a-1) == dsu.find(b-1):
                print(t)
                break
            

N, M, Q = map(int, input().split())
pairs = [list(map(int, input().split())) for _ in range(M)]
queries = [tuple(map(int, input().split())) for _ in range(Q)]

earliest_communication_times(N, M, Q, pairs, queries)
