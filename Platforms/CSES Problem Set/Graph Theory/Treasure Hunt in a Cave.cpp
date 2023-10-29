#include <bits/stdc++.h>
using namespace std;

#define MAX_NUM 1001

int n, m;
queue<pair<int, int>> q;
bool visited[MAX_NUM][MAX_NUM];
char dis[MAX_NUM][MAX_NUM];
char grid[MAX_NUM][MAX_NUM];
pair<int, int> previosNode[MAX_NUM][MAX_NUM];
int a, b, t;

int neighborX[4] = {0, 0, 1, -1};
int neighborY[4] = {1, -1, 0, 0};

bool isValid(int y, int x)
{
    if (y < 1)
        return false;
    if (x < 1)
        return false;
    if (y > n)
        return false;
    if (x > m)
        return false;
    if (grid[y][x] == '1')
        return false;
    return true;
}

int main()
{
    char c;
    cin >> n >> m;

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            cin >> c;
            grid[i][j] = c;
            dis[i][j] = '_';
            visited[i][j] = false;
        }
    }

    cin >> a >> b;
    visited[a][b] = true;
    dis[a][b] = '$';
    q.push(make_pair(a, b));
    previosNode[a][b] = make_pair(0, 0);

    int x;
    int y;
    ;
    while (!q.empty())
    {
        pair<int, int> cc = q.front();
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            x = cc.first + neighborX[i];
            y = cc.second + neighborY[i];

            if (visited[x][y] || !isValid(x, y))
                continue;

            visited[x][y] = true;

            if (i == 0)
                dis[x][y] = 'W';
            else if (i == 1)
                dis[x][y] = 'E';
            else if (i == 2)
                dis[x][y] = 'N';
            else if (i == 3)
                dis[x][y] = 'S';

            previosNode[x][y] = make_pair(cc.first, cc.second);

            pair<int, int> new_cc{x, y};
            q.push(new_cc);
        }
    }

    //     for (int i = 1; i <= n; i++)
    //     {
    //         for (int j = 1; j <= m; j++)
    //         {
    //             cout << dis[i][j] << " ";
    //         }

    //         cout << endl;
    //     }

    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> x >> y;

        string path = "";

        if (visited[x][y])
        {
            while (dis[x][y] != '$')
            {
                path += dis[x][y];
                int temp = x;
                x = previosNode[x][y].first;
                y = previosNode[temp][y].second;
            }

            cout << path << endl;
        }
        else
            cout << "IMPOSSIBLE" << endl;
    }

    return 0;
}