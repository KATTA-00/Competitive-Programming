#include <bits/stdc++.h>
using namespace std;
// The Hamiltonian cycle of undirected graph
// Number of vertices in the graph
int N;
// int path[V];
vector<int> path;

void printSolution(vector<int> path);

bool isSafe(int v, vector<vector<bool>> graph, int pos)
{
    if (graph[path[pos - 1]][v] == 0)
        return false;

    for (int i = 0; i < pos; i++)
        if (path[i] == v)
            return false;

    return true;
}

bool hamCycleUtil(vector<vector<bool>> graph, int pos)
{
    if (pos == N)
    {
        if (graph[path[pos - 1]][path[0]] == 1)
            return true;
        else
            return false;
    }

    for (int v = 1; v < N; v++)
    {

        if (isSafe(v, graph, pos))
        {
            path[pos] = v;
            if (hamCycleUtil(graph, pos + 1) == true)
                return true;

            path[pos] = -1;
        }
    }

    return false;
}

bool hamCycle(vector<vector<bool>> graph)
{
    for (int i = 0; i < N; i++)
        path.push_back(-1);

    path[0] = 0;
    if (hamCycleUtil(graph, 1) == false)
    {
        cout << "\nSolution does not exist";
        return false;
    }

    printSolution(path);
    return true;
}

/* A utility function to print solution */
void printSolution(vector<int> path)
{
    cout << "Solution Exists:"
            " Following is one Hamiltonian Cycle \n";

    for (int i = 0; i < N; i++)
        cout << path[i] << " ";

    // Let us print the first vertex again
    // to show the complete cycle
    cout << path[0] << " ";
    cout << endl;
}

// Driver Code
int main()
{
    N = 5;
    vector<vector<bool>> graph1 = {{0, 1, 0, 1, 0},
                                   {1, 0, 1, 1, 1},
                                   {0, 1, 0, 0, 1},
                                   {1, 1, 0, 0, 1},
                                   {0, 1, 1, 1, 0}};

    // Print the solution
    hamCycle(graph1);

    vector<vector<bool>> graph2 = {{0, 1, 0, 1, 0},
                                   {1, 0, 1, 1, 1},
                                   {0, 1, 0, 0, 1},
                                   {1, 1, 0, 0, 0},
                                   {0, 1, 1, 0, 0}};

    // Print the solution
    hamCycle(graph2);

    return 0;
}
