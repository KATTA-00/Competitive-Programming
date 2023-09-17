#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define MAX 501

int n, m;
int grid[MAX][MAX];
int c;

bool checkValid(int x, int y)
{
    if (y >= n)
        return false;
    else if (grid[x][y] == 2 || grid[x][y] == 1)
        return false;
    else
        return true;
}

int main()
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    cin >> n >> m;
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> c;
            grid[i][j] = c;
        }
    }

    int y;
    for (int j = n - 2; j >= 0; j--)
    {

        for (int i = 0; i < m; i++)
        {
            y = j;
            if (grid[i][y] != 2)
                continue;

            while (checkValid(i, y + 1))
            {
                grid[i][y] = 0;
                grid[i][y + 1] = 2;
                y++;
            }
        }
    }

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << grid[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
