#include <bits/stdc++.h>
using namespace std;

#include <map>
#define MAX_N 20001

struct Node
{
    vector<int> adj;
    vector<int> rev_adj;
};

int n, m;
Node g[MAX_N];
bool visited[MAX_N];
stack<int> S;
int numComponents;

void dfs_1(int x)
{
    visited[x] = true;
    for (long long unsigned int i = 0; i < g[x].adj.size(); i++)
    {
        if (!visited[g[x].adj[i]])
        {
            dfs_1(g[x].adj[i]);
        }
    }
    S.push(x);
}

void dfs_2(int x)
{
    visited[x] = true;
    for (long long unsigned int i = 0; i < g[x].rev_adj.size(); i++)
    {
        if (!visited[g[x].rev_adj[i]])
            dfs_2(g[x].rev_adj[i]);
    }
}

void Kosaraju(int node)
{
    for (int i = 0; i < node; i++)
    {
        if (!visited[i])
        {
            dfs_1(i);
        }
    }

    for (int i = 0; i < node; i++)
        visited[i] = false;

    while (!S.empty())
    {
        int v = S.top();
        S.pop();
        if (!visited[v])
        {
            dfs_2(v);
            numComponents++;
        }
    }
}

int getKey(int i, int j)
{
    return i * m + j;
}

int main()
{
    cin >> n >> m;
    char grid[n][m];
    char c;
    int node = 0;
    map<int, int> mmap;

    int count = 0;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> c;
            grid[i][j] = c;

            if (c == '.')
            {
                mmap[count] = node;
                node++;
            }

            count++;
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (grid[i][j] == '.')
            {
                if ((i - 1 >= 0) && (grid[i - 1][j] == '.'))
                {
                    g[mmap[getKey(i, j)]].adj.push_back(mmap[getKey(i - 1, j)]);
                    g[mmap[getKey(i - 1, j)]].rev_adj.push_back(mmap[getKey(i, j)]);
                }
                if ((i + 1 < n) && (grid[i + 1][j] == '.'))
                {
                    g[mmap[getKey(i, j)]].adj.push_back(mmap[getKey(i + 1, j)]);
                    g[mmap[getKey(i + 1, j)]].rev_adj.push_back(mmap[getKey(i, j)]);
                }
                if ((j - 1 >= 0) && (grid[i][j - 1] == '.'))
                {
                    g[mmap[getKey(i, j)]].adj.push_back(mmap[getKey(i, j - 1)]);
                    g[mmap[getKey(i, j - 1)]].rev_adj.push_back(mmap[getKey(i, j)]);
                }
                if ((j + 1 < m) && (grid[i][j + 1] == '.'))
                {
                    g[mmap[getKey(i, j)]].adj.push_back(mmap[getKey(i, j + 1)]);
                    g[mmap[getKey(i, j + 1)]].rev_adj.push_back(mmap[getKey(i, j)]);
                }
            }
        }
    }

    Kosaraju(node);
    printf("%d\n", numComponents);

    return 0;
}