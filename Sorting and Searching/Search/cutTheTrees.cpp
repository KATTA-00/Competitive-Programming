#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> adj;
vector<int> values;
vector<int> visited;
int totalSum = 0;
int minDifference = INT_MAX;

int dfs(int node) {
    visited[node] = 1;
    int subtreeSum = values[node];

    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            subtreeSum += dfs(neighbor);
        }
    }

    int remainingSum = totalSum - subtreeSum;
    minDifference = min(minDifference, abs(subtreeSum - remainingSum));
    return subtreeSum;
}

int cutTheTree(vector<int> data, vector<vector<int>> edges) {
    int n = data.size();
    adj.resize(n);
    values = data;
    visited.assign(n, 0);

    for (vector<int> edge : edges) {
        int u = edge[0] - 1;
        int v = edge[1] - 1;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    for (int i = 0; i < n; i++) {
        totalSum += data[i];
    }

    dfs(0);
    return minDifference;
}

int main() {
    int n;
    cin >> n;
    vector<int> data(n);

    for (int i = 0; i < n; i++) {
        cin >> data[i];
    }

    vector<vector<int>> edges(n - 1);

    for (int i = 0; i < n - 1; i++) {
        edges[i].resize(2);

        for (int j = 0; j < 2; j++) {
            cin >> edges[i][j];
        }
    }

    int result = cutTheTree(data, edges);
    cout << result << "\n";

    return 0;
}
