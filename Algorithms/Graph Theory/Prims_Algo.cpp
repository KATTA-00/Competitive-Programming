#include <bits/stdc++.h>
using namespace std;

const int MAX = 3e3 + 1;
int N, M;
int graph[MAX][MAX];

int getMinKey(int key[], bool minimumSet[])
{
    int min = INT_MAX;
    int min_index;

    for (int v = 0; v < N; v++)
        if (minimumSet[v] == false && key[v] < min)
            min = key[v], min_index = v;

    return min_index;
}

int primsAlgorithm(int graph[MAX][MAX])
{
    int parent[N];
    int key[N];
    bool minimumSet[N];

    for (int i = 0; i < N; i++)
        key[i] = INT_MAX, minimumSet[i] = false;

    key[0] = 0;
    parent[0] = -1;

    for (int count = 0; count < N - 1; count++)
    {
        int u = getMinKey(key, minimumSet);

        minimumSet[u] = true;

        for (int v = 0; v < N; v++)

            if (graph[u][v] && minimumSet[v] == false && graph[u][v] < key[v])
                parent[v] = u, key[v] = graph[u][v];
    }

    int sum = 0;
    for (int i = 0; i < N; i++)
    {
        sum += graph[i][parent[i]];
    }

    return sum;
}

int main()
{
    cin >> N >> M;

    int a, b, w;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            graph[i][j] = 0;
        }
    }

    for (int i = 0; i < M; i++)
    {
        cin >> a >> b >> w;
        graph[a - 1][b - 1] = w;
        graph[b - 1][a - 1] = w;
    }

    cout << primsAlgorithm(graph) << endl;

    return 0;
}
