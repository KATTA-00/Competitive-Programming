#include <bits/stdc++.h>
using namespace std;
#define SZ 200005

const int maxN = 1e5 + 1;
const int logN = 25;
int N, Q, k, x;
int L[SZ];
vector<int> adj[SZ];
int jump[21][SZ];
bool colour[maxN];

void dfs(int u, int p, int l)
{
    jump[0][u] = p;

    L[u] = l;

    for (int v : adj[u])
        if (v != p)
        {
            if (colour[v])
                dfs(v, u, l + 1);
            else
                dfs(v, u, l);
        }
}

void pre()
{
    dfs(1, -1, 0);

    for (int i = 1; 1 << i <= N; i++)
        for (int j = 0; j <= N; j++)
            jump[i][j] = jump[i - 1][jump[i - 1][j]];
}

int LCA(int p, int q)
{
    if (L[p] < L[q])
        swap(p, q);

    int diff = L[p] - L[q];

    for (int i = 20; i >= 0; i--)
        if (diff & (1 << i))
            p = jump[i][p];

    if (p == q)
        return p;

    for (int i = 20; i >= 0; i--)
    {
        if (jump[i][p] != jump[i][q])
        {
            p = jump[i][p];
            q = jump[i][q];
        }
    }

    return jump[0][p];
}

int main()
{
    int a, b;
    cin >> N >> Q;

    for (int i = 1; i <= N; i++)
    {
        cin >> colour[i];
    }

    int t;
    for (int i = 2; i <= N; i++)
    {
        cin >> t;
        adj[i].push_back(t);
        adj[t].push_back(i);
    }

    pre();

    while (Q--)
    {

        cin >> a >> b;
        int t = 0;
        if ((a == 1 || b == 1) && colour[1])
            t++;
        int lca = LCA(a, b);

        cout << t + L[a] + L[b] - 2 * L[lca] << endl;
    }
}