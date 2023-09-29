#include <bits/stdc++.h>
using namespace std;

#define MAX 5001
int n, m, d, q;
int a, b, w;
int grid[MAX][MAX];
int dis[MAX][MAX];

int main()
{
    cin >> n >> m;

    for (int i = 0; i < m; i++)
    {
        cin >> a >> b >> w;
        grid[a][b] = w;
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
                dis[i][j] = INT_MAX;
        }
    }

    // run the algorithm
    for (int k = 1; k <= n; k++)
    {
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]);
            }
        }
    }

    cin >> d >> q;

    for (int i = 0; i < q; i++)
    {
        cin >> a;
        if (dis[a][d] == INT_MAX)
            cout << "Impossible" << endl;
        else
            cout << dis[a][b] << endl;
    }

    return 0;
}