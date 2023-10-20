#include <bits/stdc++.h>
using namespace std;

#define MAX_NUM 100001
vector<int> adj[MAX_NUM];
bool visited[MAX_NUM];
int dis[MAX_NUM];
int parent[MAX_NUM];
int n, m;

int main()
{
    cin >> n >> m;

    int a, b;
    for (int i = 0; i < m; i++)
    {
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    fill(begin(visited), begin(visited) + n + 1, false);

    queue<int> Q;
    Q.push(1);
    parent[1] = -1;
    dis[1] = 1;
    visited[1] = true;

    while (!Q.empty())
    {
        int u = Q.front();
        Q.pop();

        for (auto element : adj[u])
        {
            if (visited[element])
                continue;

            Q.push(element);
            parent[element] = u;
            dis[element] = dis[u] + 1;

            visited[element] = true;
        }
    }

    // for (int i = 0; i < 10; i++)
    // {
    //     cout << parent[i] << " ";
    // }
    // cout << endl;

    vector<int> path;
    int c = dis[n];
    if (visited[n])
    {
        cout << c << endl;

        while (n != -1)
        {
            path.push_back(n);
            n = parent[n];
        }

        // for (int i = 0; i < c; i++)
        // {
        //     cout << path[i] << "$";
        // }

        for (int i = c - 1; i > -1; i--)
            cout << path[i] << " ";

        cout << endl;
    }
    else
        cout << "IMPOSSIBLE" << endl;

    return 0;
}