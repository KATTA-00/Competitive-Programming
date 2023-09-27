'''

Given a weighted, undirected and connected graph of V vertices and an adjacency list adj where adj[i] is 
a list of lists containing two integers where the first integer of each list j denotes there is edge 
between i and j , second integers corresponds to the weight of that  edge . You are given the source 
vertex S and You to Find the shortest distance of all the vertex's from the source vertex S. 
You have to return a list of integers denoting shortest distance between each node and Source vertex S.

Input:
V = 3, E = 3
adj = {{{1, 1}, {2, 6}}, {{2, 3}, {0, 1}}, {{1, 3}, {0, 6}}}
S = 2

Output:
4 3 0

         0
    1  /   \  6
      /     \
    1 ------- 2
         3   

Explanation:

For nodes 2 to 0, we can follow the path-
2-1-0. This has a distance of 1+3 = 4,
whereas the path 2-0 has a distance of 6. So,
the Shortest path from 2 to 0 is 4.
The shortest distance from 0 to 1 is 1 .

'''


class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex S.
    def dijkstra(self, V, adj, S):
        import heapq

        # Initialize distances with infinity for all nodes except the source node.
        distances = [float('inf')] * V
        distances[S] = 0

        # Create a priority queue to store nodes to visit.
        priority_queue = [(0, S)]

        while priority_queue:
            # Get the node with the smallest distance from the priority queue.
            current_distance, current_node = heapq.heappop(priority_queue)

            # If the current distance is greater than the recorded distance, skip it.
            if current_distance > distances[current_node]:
                continue

            # Explore neighbors of the current node.
            for neighbor, weight in adj[current_node]:
                distance = current_distance + weight

                # If the new distance is smaller than the recorded distance, update it.
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
