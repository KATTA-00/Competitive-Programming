# A recursive function used by longestPath. See below
# link for details
# https:#www.geeksforgeeks.org/topological-sorting/
def topologicalSortUtil(v):
	global Stack, visited, adj
	visited[v] = True

	# Recur for all the vertices adjacent to this vertex
	# list<AdjListNode>::iterator i
	for i in adj[v]:
		if (not visited[i[0]]):
			topologicalSortUtil(i[0])

	# Push current vertex to stack which stores topological
	# sort
	Stack.append(v)

# The function to find longest distances from a given vertex.
# It uses recursive topologicalSortUtil() to get topological
# sorting.
def longestPath(s):
	global Stack, visited, adj, V
	dist = [-10**9 for i in range(V)]

	# Call the recursive helper function to store Topological
	# Sort starting from all vertices one by one
	for i in range(V):
		if (visited[i] == False):
			topologicalSortUtil(i)
	# print(Stack)

	# Initialize distances to all vertices as infinite and
	# distance to source as 0
	dist[s] = 0
	# Stack.append(1)

	# Process vertices in topological order
	while (len(Stack) > 0):
	
		# Get the next vertex from topological order
		u = Stack[-1]
		del Stack[-1]
		#print(u)

		# Update distances of all adjacent vertices
		# list<AdjListNode>::iterator i
		if (dist[u] != 10**9):
			for i in adj[u]:
				# print(u, i)
				if (dist[i[0]] < dist[u] + i[1]):
					dist[i[0]] = dist[u] + i[1]

	# Print calculated longest distances
	# print(dist)
	for i in range(V):
		print("INF ",end="") if (dist[i] == -10**9) else print(dist[i],end=" ")


row = int(input())
V, Stack, visited = row*row, [], [False for i in range(7)]
adj = [[[[] for j in range(row)]] for i in range(row)]

for i in range(row):
	data = [int(x) for x in input().strip().split(" ")]
	for j in range(1, row):
		adj[i][j-1].append([[i, j], data[j]])

for i in range(row):
	print(i)

# s = 1
# print("Following are longest distances from source vertex ",s)
# longestPath(s)

	# This code is contributed by mohit kumar 29.
