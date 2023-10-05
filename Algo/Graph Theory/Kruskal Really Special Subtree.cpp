#include <bits/stdc++.h>

using namespace std;
const int MAX = 3e3 + 1;
int n, m;

class myDSU
{
    int parent[MAX];
    int rank[MAX];

public:
    myDSU(int n)
    {

        for (int i = 0; i < n; i++)
        {
            parent[i] = -1;
            rank[i] = 1;
        }
    }

    int find(int i)
    {
        if (parent[i] == -1)
            return i;

        return parent[i] = find(parent[i]);
    }

    void unite(int x, int y)
    {
        int s1 = find(x);
        int s2 = find(y);

        if (s1 != s2)
        {
            if (rank[s1] < rank[s2])
            {
                parent[s1] = s2;
            }
            else if (rank[s1] > rank[s2])
            {
                parent[s2] = s1;
            }
            else
            {
                parent[s2] = s1;
                rank[s1] += 1;
            }
        }
    }
};

class Graph
{
    vector<vector<int>> edgelist;
    int V;

public:
    Graph(int V) { this->V = V; }

    void addEdge(int x, int y, int w)
    {
        edgelist.push_back({w, x, y});
    }

    int kruskals_mst()
    {
        sort(edgelist.begin(), edgelist.end());

        myDSU s(V);
        int ans = 0;

        for (auto edge : edgelist)
        {
            int w = edge[0];
            int x = edge[1];
            int y = edge[2];

            if (s.find(x) != s.find(y))
            {
                s.unite(x, y);
                ans += w;
            }
        }

        return ans;
    }
};

int main()
{
    cin >> n >> m;
    int a, b, w;

    Graph g(n);
    for (int i = 0; i < m; i++)
    {
        cin >> a >> b >> w;
        g.addEdge(a - 1, b - 1, w);
    }

    cout << g.kruskals_mst();
    return 0;
}