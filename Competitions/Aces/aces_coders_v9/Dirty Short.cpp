#include <bits/stdc++.h>
using namespace std;
const int MAX = 2e3 + 1;
vector<vector<int>> grid;
bool visited[MAX];
char colour[MAX];
int t, n, m, a, b;

int dfs(int n)
{

    visited[n] = true;

    for (auto i : grid[n])
    {
        if (visited[i])
        {
            if (colour[i] == colour[n])
            {
                cout << "YES" << endl;
                return 1;
            }
        }
        else
        {
            colour[i] = (colour[n] == 1) ? 2 : 1;
            if (dfs(i) == 1)
                return 1;
        }
    }

    return 0;
}

int main()
{
    cin >> t;

    for (int k = 0; k < t; k++)
    {

        cin >> n >> m;
        grid.clear();
        for (int i = 0; i < n; i++)
        {
            grid.push_back(vector<int>(0));
        }

        for (int i = 0; i < m; i++)
        {
            cin >> a >> b;
            grid[a - 1].push_back(b - 1);
        }

        fill(begin(visited), begin(visited) + n, false);
        fill(begin(colour), begin(colour) + n, 0);

        colour[0] = 1;

        if (dfs(0) == 0)
        {
            if (visited[n - 1])
                cout << "NO" << endl;
            else
                cout << "YES" << endl;
        }
    }

    return 0;
}