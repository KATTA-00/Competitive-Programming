#include <bits/stdc++.h>
using namespace std;

const int maxN = 2e5 + 1;
const int logN = 20;
int N, Q, a, b, p[maxN][logN];
int timer, d[maxN], in[maxN], out[maxN];
vector<int> G[maxN];
bool colour[maxN];

void dfs(int u = 1, int par = 1)
{
    in[u] = ++timer;

    if (colour[u])
        d[u] = d[par] + 1;
    else
        d[u] = d[par];

    p[u][0] = par;

    for (int i = 1; i < logN; i++)
        p[u][i] = p[p[u][i - 1]][i - 1];

    for (int v : G[u])
        if (v != par)
            dfs(v, u);

    out[u] = ++timer;
}

bool anc(int u, int v)
{
    return in[u] <= in[v] && out[u] >= out[v];
}

int lca(int u, int v)
{
    if (anc(u, v))
        return u;

    if (anc(v, u))
        return v;

    for (int i = logN - 1; i >= 0; i--)
        if (!anc(p[u][i], v))
            u = p[u][i];

    return p[u][0];
}

int main()
{
    cin >> N >> Q;

    for (int i = 1; i <= N; i++)
    {
        cin >> colour[i];
    }

    int t;
    for (int i = 2; i <= N; i++)
    {
        cin >> t;
        G[i].push_back(t);
        G[t].push_back(i);
    }

    dfs();

    for (int q = 0; q < Q; q++)
    {
        cin >> a >> b;

        int t = 0;
        if (a == 1 || b == 1)
            t++;

        cout << t + d[a] + d[b] - 2 * d[lca(a, b)] << endl;
    }
}