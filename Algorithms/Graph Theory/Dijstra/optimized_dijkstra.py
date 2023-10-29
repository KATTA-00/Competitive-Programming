def optimized_djikstra(graph,start,end):
    
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
    #print(shortest_distance)
    #print(unseenNodes)
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
                #print(minNode)
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
                #print(minNode)
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
                #print(shortest_distance)
                #print(predecessor)
        unseenNodes.pop(minNode)
    currentNode = end
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
            #print(path)
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0,start)
    if shortest_distance[end] != infinity:
        #print('Shortest distance is ' + str(shortest_distance[end]))
        #print('And the path is ' + str(path))
        return shortest_distance[end]
    return None

graph = {'A': {'B': 10, 'C': 3},
        'B': {'C': 1, 'D': 2},
        'C': {'B': 4, 'D': 8, 'E': 2},
        'D': {'E': 7},
        'E': {'D': 9}}
start = 'A'
end = 'D'

print(optimized_djikstra(graph,start,end))

