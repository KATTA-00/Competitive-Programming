#include <bits/stdc++.h>
#include <map>
#include <iostream>
#include <fstream>

using namespace std;
#define ll long long int
#define MAX_N 200001

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

int concat(int a, int b)
{

    // Convert both the integers to string
    string s1 = to_string(a);
    string s2 = to_string(b);

    // Concatenate both strings
    string s = s1 + s2;

    // Convert the concatenated string
    // to integer
    int c = stoi(s);

    // return the formed integer
    return c;
}

void dfs_1(int x)
{
    visited[x] = true;
    for (long long unsigned int i = 0; i < g[x].adj.size(); i++)
    {
        if (!visited[g[x].adj[i]])
            dfs_1(g[x].adj[i]);
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
        if (!visited[i])
            dfs_1(i);

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

int main()
{
    // cin >> n >> m;
    ifstream myfile("test_input.txt");

    string mystring;
    getline(myfile, mystring, ' ');
    n = stoi(mystring);
    getline(myfile, mystring);
    m = stoi(mystring);

    char grid[n][m];
    char c;
    int node = 0;
    map<int, int> mmap;

    char ch;

    while (myfile >> noskipws >> ch)
    {
        cout << ch; // Or whatever
    }

    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < m; j++)
    //     {
    //         cin >> c;
    //         grid[i][j] = c;

    //         if (c == '.')
    //         {
    //             mmap[concat(i, j)] = node;
    //             node++;
    //         }
    //     }
    // }

    myfile.close();

    return 0;
}