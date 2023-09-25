#include <iostream>
#include <vector>
#include <climits>

using namespace std;

#define MAX 5005

vector<vector<int>> edge;
int N, M, D, Q;
int distances[MAX];
const int INF = INT_MAX; // Use INT_MAX for infinity

int bellman(int start, int end)
{
    int n = N;
    fill(distances, distances + n, INF); // Initialize distances with INF
    distances[start] = 0;

    for (int i = 0; i < n - 1; i++)
    {
        for (auto e : edge)
        {
            int a, b, w;
            a = e[0];
            b = e[1];
            w = e[2];
            if (distances[a] != INF && distances[a] + w < distances[b])
            {
                distances[b] = distances[a] + w;
            }
        }
    }

    // for (auto e : edge)
    // {
    //     int a, b, w;
    //     a = e[0];
    //     b = e[1];
    //     w = e[2];
    //     if (distances[a] != INF && distances[a] + w < distances[b])
    //     {
    //         return -1;
    //     }
    // }

    return distances[end];
}

int main()
{
    cin >> N >> M;

    for (int i = 0; i < M; i++)
    {
        int u, v, w;
        cin >> u >> v >> w;
        edge.push_back({u - 1, v - 1, w});
    }

    cin >> D >> Q;
    int c;

    for (int i = 0; i < Q; i++)
    {
        cin >> c;
        int distance = bellman(c - 1, D - 1);

        if (distance == INF)
        {
            cout << "Impossible" << endl;
        }
        else
        {
            cout << distance << endl;
        }
    }

    return 0;
}
