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

    for (int i = 1; i <= row; i++)
    {
        for (int j = 1; j <= row; j++)
        {
            cout << grid[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}

// 4 3
// .*..
// *.**
// **..
// ****