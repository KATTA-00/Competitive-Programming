from collections import defaultdict
from collections import deque


def bfs(graph, start, visited, path, startLevel):

    queue = deque()
    path.append([start, startLevel])
    queue.append([start, startLevel])
    visited[start] = True
    tempLevel = startLevel
    startLevel += 1

    while len(queue) != 0:
        tempnode = queue.popleft()
        if (tempLevel != tempnode[1]):
            tempLevel = tempnode[1]
            startLevel += 1
        tempnode = tempnode[0]

        for neighbour in graph[tempnode]:
            if visited[neighbour] == False:
                path.append([neighbour, startLevel])
                queue.append([neighbour, startLevel])
                visited[neighbour] = True

    return path


v, e = map(int, input().split())
graph = defaultdict(list)
for i in range(e):
    u, v = map(str, input().split())
    graph[u].append(v)
    graph[v].append(u)

path = []
start = 'A'
startLevel = 1
visited = defaultdict(bool)
travelsPath = bfs(graph, start, visited, path, startLevel)
print(travelsPath)
