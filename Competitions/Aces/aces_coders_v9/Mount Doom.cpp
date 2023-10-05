#include <bits/stdc++.h>
using namespace std;

const int MAX = 2e5 + 1;

vector<vector<int>> grid;
bool visited[MAX];
int magma[MAX];
int t, n, a, b, m, val;
int c;

int dfs(int n)
{
    visited[n] = true;
    c++;

    for (auto i : grid[n])
    {
        if (!visited[i])
        {
            dfs(i);
        }
    }

    return 0;
}

int main()
{
    cin >> t;

    for (int k = 0; k < t; k++)
    {

        cin >> n;
        grid.clear();
        for (int i = 0; i < n; i++)
        {
            grid.push_back(vector<int>(0));
        }

        for (int i = 0; i < n; i++)
        {
            cin >> magma[i];
        }

        for (int i = 0; i < n - 1; i++)
        {
            cin >> a >> b;
            if (magma[a - 1] > magma[b - 1])
                grid[a - 1].push_back(b - 1);
            else if ((magma[a - 1] < magma[b - 1]))
                grid[b - 1].push_back(a - 1);
        }

        m = -1;
        for (int i = 0; i < n; i++)
        {
            fill(begin(visited), begin(visited) + n, false);
            c = 0;
            dfs(i);

            if (c > m)
            {
                m = c;
                val = i;
            }
        }

        cout << val + 1 << " " << m << endl;
    }

    return 0;
}