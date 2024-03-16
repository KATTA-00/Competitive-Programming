#include <bits/stdc++.h>
using namespace std;

#define MAX_NUM 1001

int n, m;
queue<pair<int, int>> q;
bool visited[MAX_NUM][MAX_NUM];
char dis[MAX_NUM][MAX_NUM];
char grid[MAX_NUM][MAX_NUM];

pair<int, int> previosNode[MAX_NUM][MAX_NUM];

int neighborX[4] = {0, 0, 1, -1};
int neighborY[4] = {1, -1, 0, 0};

bool isValid(int y, int x)
{
    if (y < 0)
        return false;
    if (x < 0)
        return false;
    if (y >= n)
        return false;
    if (x >= m)
        return false;
    if (grid[y][x] == '#')
        return false;
    return true;
}

int main()
{
    char c;
    cin >> n >> m;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> c;
            grid[i][j] = c;
            dis[i][j] = '_';
            visited[i][j] = false;

            if (c == 'T')
            {
                visited[i][j] = true;
                q.push(make_pair(i, j));
                previosNode[i][j] = make_pair(0, 0);
            }
        }
    }

    int x;
    int y;
    bool flag = false;
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
                dis[x][y] = 'R';
            else if (i == 1)
                dis[x][y] = 'L';
            else if (i == 2)
                dis[x][y] = 'D';
            else if (i == 3)
                dis[x][y] = 'U';

            previosNode[x][y] = make_pair(cc.first, cc.second);

            if (grid[x][y] == 'J')
            {
                flag = true;
                break;
            }

            pair<int, int> new_cc{x, y};
            q.push(new_cc);
        }

        if (flag)
            break;
    }

    string path = "";

    if (flag)
    {
        cout << "YES" << endl;

        while (grid[x][y] != 'T')
        {
            path += dis[x][y];
            int temp = x;
            x = previosNode[x][y].first;
            y = previosNode[temp][y].second;
        }

        cout << path.length() << endl;
    }
    else
        cout << "IMPOSSIBLE" << endl;

    return 0;
}