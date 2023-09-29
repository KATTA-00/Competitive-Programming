#include <bits/stdc++.h>

using namespace std;

#define MAX 1001

int grid[MAX][MAX];
int row, q;
char c;

int countGrid(int x, int y, char ch)
{
    if (x == 1 && y == 1)
    {
        return ((ch == '.') ? 0 : 1);
    }
    else if (x == 1)
    {
        return grid[x][y - 1] + ((ch == '.') ? 0 : 1);
    }
    else if (y == 1)
    {
        return grid[x - 1][y] + ((ch == '.') ? 0 : 1);
    }
    else
    {
        return grid[x - 1][y] - grid[x - 1][y - 1] + grid[x][y - 1] + ((ch == '.') ? 0 : 1);
    }
}

int getSum(int x, int y, int x_, int y_)
{

    if (x == 1 && y == 1)
    {
        return grid[x_][y_];
    }
    else if (x == 1)
    {
        if (x_ == 1)
        {
            return grid[x_][y_] - grid[x][y - 1];
        }
        else
        {
            return grid[x_][y_] - grid[x_][y - 1];
        }
    }
    else if (y == 1)
    {
        if (y_ == 1)
        {
            return grid[x_][y_] - grid[x - 1][y];
        }
        else
        {
            return grid[x_][y_] - grid[x - 1][y_];
        }
    }
    else
    {
        return grid[x_][y_] - grid[x - 1][y_] - grid[x_][y - 1] + grid[x - 1][y - 1];
    }
}

int main()
{
    cin >> row >> q;

    for (int i = 1; i <= row; i++)
    {
        for (int j = 1; j <= row; j++)
        {
            cin >> c;
            grid[i][j] = countGrid(i, j, c);
        }
    }

    int x, y, x_, y_;

    for (int i = 0; i < q; i++)
    {
        cin >> x >> y >> x_ >> y_;
        cout << getSum(x, y, x_, y_) << endl;
    }

    // for (int i = 1; i <= row; i++)
    // {
    //     for (int j = 1; j <= row; j++)
    //     {
    //         cout << grid[i][j] << " ";
    //     }
    //     cout << endl;
    // }

    return 0;
}

// 4 3
// .*..
// *.**
// **..
// ****