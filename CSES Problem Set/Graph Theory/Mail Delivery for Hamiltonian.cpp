#include <bits/stdc++.h>
using namespace std;
int N, M;
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

void printSolution(vector<int> path)
{
    for (int i = 0; i < N; i++)
        cout << path[i] << " ";

    cout << path[0] << " ";
    cout << endl;
}

int main()
{
    cin >> N >> M;
    vector<vector<bool>> graph1;

    for (int i = 0; i < N; i++)
    {
        vector<bool> t(N);
        fill(begin(t), begin(t) + N, false);
        graph1.push_back(t);
    }

    int a, b;
    for (int i = 0; i < M; i++)
    {
        cin >> a >> b;
        graph1[a - 1][b - 1] = true;
        graph1[b - 1][a - 1] = true;
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cout << graph1[i][j] << " ";
        }
        cout << endl;
    }

    hamCycle(graph1);

    return 0;
}
