#include <bits/stdc++.h>
using namespace std;

#define MAX_NUM 100001

int n, m;
vector<int> adj[MAX_NUM];
bool visited[MAX_NUM];
vector<vector<int>> components;
int component = 0;

void dfs(int s)
{
    components[component].push_back(s);
    visited[s] = true;
    for (auto u : adj[s])
    {
        if (visited[u])
            continue;
        dfs(u);
    }
}

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

    for (int i = 1; i <= n; i++)
    {
        visited[i] = false;
    }

    for (int i = 1; i <= n; i++)
    {
        if (!visited[i])
        {
            components.push_back(vector<int>{});
            dfs(i);
            component++;
        }
    }

    cout << component - 1 << endl;

    for (int i = 0; i < component - 1; i++)
    {
        cout << components[i][0] << " " << components[i + 1][0] << endl;
    }

    return 0;
}