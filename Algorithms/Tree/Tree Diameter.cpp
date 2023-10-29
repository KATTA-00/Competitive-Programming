#include <bits/stdc++.h>
using namespace std;

#define MAX 200001

vector<int> g[MAX];
int dis[MAX];
int N;
int a, b;

void dfs(int u, int p)
{

    for (auto v : g[u])
    {
        if (p != v)
        {
            dis[v] = dis[u] + 1;
            dfs(v, u);
        }
    }
}

int main()
{
    cin >> N;
    for (int i = 0; i < N - 1; i++)
    {
        cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
    }

    dis[1] = 0;
    dfs(1, 0);

    int max = 1;
    for (int i = 1; i <= N; i++)
    {
        if (dis[max] < dis[i])
            max = i;
    }

    dis[max] = 0;
    dfs(max, 0);

    max = 1;
    for (int i = 1; i <= N; i++)
    {
        if (dis[max] < dis[i])
            max = i;
    }

    cout << dis[max];

    return 0;
}
