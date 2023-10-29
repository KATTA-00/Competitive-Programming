#include <bits/stdc++.h>
using namespace std;

unordered_set<string> seen;
vector<int> edges;
int n;

void dfs(string node, int &k, string &A)
{
    for (int i = 0; i < k; ++i)
    {
        string str = node + A[i];
        if (seen.find(str) == seen.end())
        {
            seen.insert(str);
            dfs(str.substr(1), k, A);
            edges.push_back(i);
        }
    }
}

string deBruijn(int n, int k, string A)
{

    seen.clear();
    edges.clear();

    string startingNode = string(n - 1, A[0]);
    dfs(startingNode, k, A);

    string S;

    int l = pow(k, n);
    for (int i = 0; i < l; ++i)
        S += A[edges[i]];
    S += startingNode;

    return S;
}

int main()
{
    cin >> n;

    int k = 2;
    string A = "01";

    cout << deBruijn(n, k, A);

    return 0;
}
