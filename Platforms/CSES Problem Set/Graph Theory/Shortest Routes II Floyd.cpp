#include <bits/stdc++.h>
using namespace std;

#define MAX 5001
#define INF LLONG_MAX // Use LLONG_MAX for a larger value
int n, m, q;
int a, b;
long long w;
long long grid[MAX][MAX];
long long dis[MAX][MAX];

int main()
{
    cin >> n >> m >> q;

    for (int i = 0; i < m; i++)
    {
        cin >> a >> b >> w;

        if (grid[a][b] == 0 || grid[a][b] > w)
        {
            grid[a][b] = w;
            k
                grid[b][a] = w;
        }
    }

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            if (i == j)
                dis[i][j] = 0;
            else if (grid[i][j])
                dis[i][j] = grid[i][j];
            else
                dis[i][j] = INF;
        }
    }

    // run the algorithm
    for (int k = 1; k <= n; k++)
    {
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                if (dis[i][k] != INF && dis[k][j] != INF)
                {
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]);
                }
            }
        }
    }

    for (int i = 0; i < q; i++)
    {
        cin >> a >> b;
        if (dis[a][b] == INF)
            cout << "-1" << endl;
        else
            cout << dis[a][b] << endl;
    }

    return 0;
}
