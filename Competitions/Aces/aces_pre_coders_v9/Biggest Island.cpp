#include <bits/stdc++.h>

using namespace std;
#define MAX 10
int grid[MAX][MAX];
bool visited[MAX][MAX];
int row, col;
int c;
int x_new, y_new;
int t;

int x_walk[] = {0, 0, 1, -1, 1, -1, 1, -1};
int y_walk[] = {1, -1, 0, 0, 1, -1, -1, 1};

bool isValid(int x, int y)
{
    if (x < 0 || y < 0 || x >= row || y >= col || grid[x][y] == 0)
        return false;

    return true;
}

void dfs(int x, int y)
{

    if (visited[x][y])
        return;

    visited[x][y] = true;
    t++;

    for (int i = 0; i < 8; i++)
    {
        x_new = x + x_walk[i];
        y_new = y + y_walk[i];

        if (isValid(x_new, y_new))
            dfs(x_new, y_new);
    }
}

int main()
{
    cin >> row;
    cin >> col;

    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            cin >> c;
            grid[i][j] = c;
        }
    }

    int max = 0;
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            t = 0;
            if (!visited[i][j] && grid[i][j] == 1)
            {
                dfs(i, j);
                if (t > max)
                    max = t;
            }
        }
    }

    cout << max << endl;

    return 0;
}