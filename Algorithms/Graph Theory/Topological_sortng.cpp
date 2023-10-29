#include <bits/stdc++.h>
using namespace std;

class Graph
{
public:
    int V;
    stack<int> Stack;
    list<int> *adj;

    // Constructor
    Graph(int V)
    {
        this->V = V;
        adj = new list<int>[V];
    }

    void topologicalSortUtil(int v, bool visited[],
                             stack<int> &Stack)
    {
        // Mark the current node as visited.
        visited[v] = true;

        list<int>::iterator i;
        for (i = adj[v].begin(); i != adj[v].end(); ++i)
            if (!visited[*i])
                topologicalSortUtil(*i, visited, Stack);

        Stack.push(v);
    }

    // function to add an edge to graph
    void addEdge(int v, int w)
    {
        // Add w to v’s list.
        adj[v].push_back(w);
    }

    void topologicalSort()
    {

        // Mark all the vertices as not visited
        bool *visited = new bool[V];
        for (int i = 0; i < V; i++)
            visited[i] = false;

        for (int i = 0; i < V; i++)
            if (visited[i] == false)
                topologicalSortUtil(i, visited, Stack);

        // Print contents of stack
        // while (Stack.empty() == false)
        // {
        //     cout << Stack.top() << " ";
        //     Stack.pop();
        // }

        delete[] visited;
    }
};

// Driver Code
int main()
{
    // Create a graph given in the above diagram
    Graph g(6);
    g.addEdge(2, 3);
    g.addEdge(4, 1);
    g.addEdge(3, 1);
    g.addEdge(5, 0);
    g.addEdge(4, 0);
    g.addEdge(5, 2);

    // Function Call
    g.topologicalSort();

    return 0;
}
