#include <bits/stdc++.h>
using namespace std;

#define V 5
int n;
int getMinKey(int key[], bool minimumSet[])
{
    // Initialize min value
    int min = INT_MAX;
    int min_index;

    for (int v = 0; v < V; v++)
        if (minimumSet[v] == false && key[v] < min)
            min = key[v], min_index = v;

    return min_index;
}

int primsAlgorithm(int graph[V][V])
{
    int parent[V];
    int key[V];
    bool minimumSet[V];

    // Initialize all keys as INFINITE
    for (int i = 0; i < V; i++)
        key[i] = INT_MAX, minimumSet[i] = false;

    key[0] = 0;
    parent[0] = -1;

    for (int count = 0; count < V - 1; count++)
    {
        int u = getMinKey(key, minimumSet);

        // Add the picked vertex to the MST Set
        minimumSet[u] = true;

        for (int v = 0; v < V; v++)

            if (graph[u][v] && minimumSet[v] == false && graph[u][v] < key[v])
                parent[v] = u, key[v] = graph[u][v];
    }

    int sum = 0;
    for (int i = 1; i < V; i++)
    {
        // cout << parent[i] << " - " << i << " \t" << graph[i][parent[i]] << " \n";
        sum += graph[i][parent[i]];
    }
    return sum;
}

// Driver's code
int main()
{
    int graph[V][V] = {{0, 2, 0, 6, 0},
                       {2, 0, 3, 8, 5},
                       {0, 3, 0, 0, 7},
                       {6, 8, 0, 0, 9},
                       {0, 5, 7, 9, 0}};

    // Print the solution
    cout << primsAlgorithm(graph) << endl;

    return 0;
}

// This code is contributed by rathbhupendra
