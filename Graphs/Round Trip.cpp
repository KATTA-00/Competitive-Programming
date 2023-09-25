#include <bits/stdc++.h>

using namespace std;
#define MAX 100001

vector<int> adj[MAX], ans;
int p[MAX], root[MAX];
int n, m;
int a, b;

void dfs(int u)
{
    for (int v : adj[u])
    {
        if (v != p[u])
        {
            p[v] = u;
            dfs(v);
        }
    }
}

int find(int u)
{
    if (root[u] < 0)
        return u;
    root[u] = find(root[u]);
    return root[u];
}

bool merge(int u, int v)
{
    u = find(u);
    v = find(v);
    if (u == v)
        return false;
    if (root[u] < root[v])
        swap(u, v);
    root[v] += root[u];
    root[u] = v;
    return true;
}

int main()
{
    cin >> n >> m;
    fill(root + 1, root + 1 + n, -1);

    for (int i = 0; i < m; i++)
    {
        cin >> a >> b;
        if (!merge(a, b))
        {
            dfs(b);

            int u = b;
            while (u != 0)
            {
                ans.push_back(u);
                u = p[u];
            }

            int K = ans.size();
            printf("%d\n", K + 1);

            for (int j = 0; j < K; j++)
                printf("%d ", ans[j]);

            printf("%d\n", b);

            return 0;
        }
        else
        {
            adj[a].push_back(b);
            adj[b].push_back(a);
        }
    }
    cout << "IMPOSSIBLE";

    return 0;
}