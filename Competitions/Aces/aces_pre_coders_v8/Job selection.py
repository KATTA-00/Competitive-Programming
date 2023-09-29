# Ford-Fulkerson algorith in Python

from collections import defaultdict

def printGraph(graph):
    for i in graph:
        print(i)

class Graph:

    def __init__(self, graph):
        self.graph = graph
        self. ROW = len(graph)


    # Using BFS as a searching algorithm 
    def searching_algo_BFS(self, s, t, parent):

        visited = [False] * (self.ROW)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    # Applying fordfulkerson algorithm
    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0

        while self.searching_algo_BFS(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Adding the path flows
            max_flow += path_flow

            # Updating the residual values of edges
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

people, job = [int(x) for x in input().split(" ")]
row = people + job + 2
graph = [[0 for x in range(row)] for y in range(row)]

for i in range(people):
    graph[0][i+1] = 1

for i in range(1, people+1):
    data = [int(x) for x in input().split(" ")]
    for j in range(job):
        graph[i][people + j + 1] = data[j]

data = [int(x) for x in input().split(" ")]
for i in range(job):
    graph[people+i+1][row-1] = data[i]


g = Graph(graph)

source = 0
sink = row - 1

print("%d " % g.ford_fulkerson(source, sink))
