'''
Alice lives in a country named Byteland. There are many cities and many uni-directional roads between them in Byteland. 
The cities are numbered from 1 to N and each road has a cost. There are M roads. 
Alice has Q friends who live in different cities of Byteland, and Alice lives in the city numbered D.
The problem is that Alice wants to find the shortest path from her friends' cities to her city. 
She asked Bob to write a program to solve the problem. Bob has written the code already, but for some reason his program is slow and buggy; 
can you help Bob to fix his code to make it efficient and bug-free?


Input Format

Each case starts with two integers, N and M. The next M lines each will contain three integers, u, v, and w, 
indicating that there is a road from u to v with cost w. Then there will be two integers, D and Q. Then there will be line with Q space-separated integers, 
denoting the cities where Alice's friends live. There can be multiple roads between two cities.

Constraints:

1 <= N <= 5000
1 <= M <= 5000
1 <= u,v <= N
u != v
1 <= w <= 1000
1 <= D <= N
1 <= Q <= N

Output Format

You need to print Q lines, each denoting the shortest path between the ith friend's city (1 <= i <= Q) and Alice's city. 
If it is not possible to go from a friend's city to Alice's city, print "Impossible" without quotation marks.

Sample Input

5 4
1 2 3
1 3 2
3 4 1
2 4 4
4 4
1 2 3 5


Sample Output

3
4
1
Impossible


'''





import heapq

def dijkstra(graph, start, end):
    n = len(graph)
    
    # Initialize distances with infinity for all nodes except the source node.
    distances = [float('inf')] * n
    distances[start] = 0
    
    # Create a priority queue to store nodes to visit.
    queue = [(0, start)]

    while queue:
         # Get the vertex with the smallest distance from the priority queue.
        current_distance, current_vertex = heapq.heappop(queue)

        # If the current distance is greater than the recorded distance, skip it.
        if current_distance > distances[current_vertex]:
            continue

        # Explore neighbors of the current node.
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # If the new distance is smaller than the recorded distance, update it.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances[end]

# Read the number of vertices (N) and edges (M) from input.
N, M = map(int, input().split())

# Create an empty adjacency list to represent the graph with N vertices.
graph = [[] for i in range(N)]

# Read the edge information and populate the adjacency list.
for i in range(M):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w))

# Read the source vertex (D) and the number of cities (Q) from input.
D, Q = map(int, input().split())
cities = list(map(int, input().split()))

for city in cities:
    # Call the dijkstra function with the graph, city - 1 (0-based index), and D - 1 as arguments.
    distance = dijkstra(graph, city - 1, D - 1)
    
    # Check if the distance is infinity (impossible to reach) and print accordingly.
    if distance == float('inf'):
        print("Impossible")
    else:
        # Print the shortest distance from the city to the source vertex.
        print(distance)
