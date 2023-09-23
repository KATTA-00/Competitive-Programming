#include <bits/stdc++.h>
using namespace std;

#define MAX 5005
vector<pair<int, int>> adj[MAX];
int grid[MAX][MAX];
int N, M, D, Q, u, v, w, t;

int main()
{
    cin >> N >> M;
    for (int i = 0; i < M; i++)
    {
        cin >> u >> v >> w;
        if (grid[u][v] == 0 || grid[u][v] > w)
        {
            grid[u][v] = w;
            grid[v][u] = w;
        }
    }

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            if (grid[i][j] != 0)
            {
                adj[i].push_back(make_pair(j, grid[i][j]));
            }
        }
    }

    cin >> D >> Q;

    int distance[N + 1];
    bool processed[N + 1];
    priority_queue<pair<int, int>> q;

    for (int i = 1; i <= N; i++)
    {
        distance[i] = INT_MAX;
        processed[i] = false;
    }

    distance[D] = 0;
    q.push({0, D}); // q - priority queue (-d,x) from node a to node b with weight w.
    while (!q.empty())
    {
        int a = q.top().second;
        int k = q.top().first;
        q.pop();

        if (processed[a])
            continue;

        if (-k > distance[a])
        {
            continue;
        }

        processed[a] = true;

        for (auto u : adj[a])
        {
            int b = u.first, w = u.second;
            if (distance[a] + w < distance[b])
            {
                distance[b] = distance[a] + w;
                q.push({-distance[b], b});
            }
        }
    }

    for (int i = 1; i <= Q; i++)
    {
        cin >> t;
        if (distance[t] == INT_MAX)
            cout << "Impossible" << endl;
        else
            cout << distance[t] << endl;
    }

    return 0;
}