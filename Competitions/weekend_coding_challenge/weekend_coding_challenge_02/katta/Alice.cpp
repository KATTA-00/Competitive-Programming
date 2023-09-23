// C program for Dijkstra's single source shortest path
// algorithm. The program is for adjacency matrix
// representation of the graph

#include <bits/stdc++.h>
using namespace std;

// Number of vertices in the graph
#define INF 9999999
#define MAX 5001
int N, M, D, Q, u, v, w, t;
int graph[MAX][MAX];

// A utility function to find the vertex with minimum
// distance value, from the set of vertices not yet included
// in shortest path tree
int minDistance(int dist[], bool sptSet[])
{
    // Initialize min value
    int min = INT_MAX, min_index;

    for (int v = 1; v <= N; v++)
        if (sptSet[v] == false && dist[v] <= min)
            min = dist[v], min_index = v;

    return min_index;
}

// A utility function to print the constructed distance
// array
void printSolution(int dist[])
{
    printf("Vertex \t\t Distance from Source\n");
    for (int i = 1; i <= N; i++)
        printf("%d \t\t\t\t %d\n", i, dist[i]);
}

// Function that implements Dijkstra's single source
// shortest path algorithm for a graph represented using
// adjacency matrix representation
void dijkstra(int src, int Q)
{
    int dist[N + 1]; // The output array. dist[i] will hold the
                     // shortest
    // distance from src to i

    bool sptSet[N + 1]; // sptSet[i] will be true if vertex i is
                        // included in shortest
    // path tree or shortest distance from src to i is
    // finalized

    // Initialize all distances as INFINITE and stpSet[] as
    // false
    for (int i = 1; i <= N; i++)
        dist[i] = INT_MAX, sptSet[i] = false;

    // Distance of source vertex from itself is always 0
    dist[src] = 0;

    // Find shortest path for all vertices
    for (int count = 1; count <= N - 1; count++)
    {
        // Pick the minimum distance vertex from the set of
        // vertices not yet processed. u is always equal to
        // src in the first iteration.
        int u = minDistance(dist, sptSet);

        // Mark the picked vertex as processed
        sptSet[u] = true;

        // Update dist value of the adjacent vertices of the
        // picked vertex.
        for (int v = 1; v <= N; v++)

            // Update dist[v] only if is not in sptSet,
            // there is an edge from u to v, and total
            // weight of path from src to v through u is
            // smaller than current value of dist[v]
            if (!sptSet[v] && graph[u][v] && dist[u] != INT_MAX && dist[u] + graph[u][v] < dist[v])
                dist[v] = dist[u] + graph[u][v];
    }

    // print the constructed distance array
    // printSolution(dist);
    for (int i = 1; i <= Q; i++)
    {
        cin >> t;
        if (dist[t] == INT_MAX)
            cout << "Impossible" << endl;
        else
            cout << dist[t] << endl;
    }
}

// driver's code
int main()
{
    cin >> N >> M;

    /* Let us create the example graph discussed above */
    for (int i = 0; i < M; i++)
    {
        cin >> u >> v >> w;
        if (graph[u][v] == 0 || graph[u][v] > w)
        {
            graph[u][v] = w;
            graph[v][u] = w;
        }
    }

    cin >> D >> Q;

    // Function call
    dijkstra(D, Q);

    return 0;
}
