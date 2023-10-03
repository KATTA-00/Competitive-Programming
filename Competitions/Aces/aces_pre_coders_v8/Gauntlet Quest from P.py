from heapq import heappush, heappop
from itertools import product


def find_distances(graph, k, n, stones):
    print("****************")
    distances = [[float('inf')]*(1 << (k)) for _ in range(n)]
    dis = 0
    node = 0
    ss = stones[0]
    heap = [(dis, node, ss)]

    target_node = n-1
    target_stone = (1 << k) - 1
    while True:
        dis, node, ss = heappop(heap)
        print(dis, node, ss)
        if (dis >= distances[node][ss]):
            continue
        distances[node][ss] = dis
        if (node == target_node and ss == target_stone):
            break
        for ch, t in graph[node]:
            new_stone = ss | stones[ch]
            new_dis = dis + t
            if (new_dis >= distances[ch][new_stone]):
                continue
            heappush(heap, (new_dis, ch, new_stone))
    print(distances[n-1])
    return distances[n-1]


def solve(distances, k):
    target = (1 << k)-1
    best = float('inf')
    for s1, d1 in enumerate(distances):
        for s2, d2 in enumerate(distances):
            stone = s1 | s2
            if (stone == target):
                best = min(best, max(d1, d2))
    return best


def solve2(distances, k):
    target = (1 << k)-1
    itt = product(enumerate(distances), enumerate(distances))
    return min((s1 | s2 != target, max(d1, d2)) for ((s1, d1), (s2, d2)) in itt)[1]


def main():
    n, m, k = map(int, input().split())
    stones = [0]*n
    graph = [[] for _ in range(n)]
    for i in range(n):
        _, *cs = map(int, input().split())
        for c in cs:
            c -= 1
            stones[i] |= 1 << c
    for _ in range(m):
        u, v, t = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((v, t))
        graph[v].append((u, t))
    distances = find_distances(graph, k, n, stones)
    print(solve2(distances, k))


main()
