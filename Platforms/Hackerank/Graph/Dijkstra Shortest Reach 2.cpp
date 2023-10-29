#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;
#define MAX 3001

typedef pair<int, int> pii;
vector<pii> graph[MAX];
int N, M, D, Q, t;
int distances[MAX];

int dijkstra(int start)
{
    int n = N;
    fill(distances, distances + n + 1, INT_MAX);
    distances[start] = 0;
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    pq.push({0, start});

    while (!pq.empty())
    {
        int current_distance = pq.top().first;
        int current_vertex = pq.top().second;
        pq.pop();

        if (current_distance > distances[current_vertex])
        {
            continue;
        }

        for (auto neighbor : graph[current_vertex])
        {
            int neighbor_vertex = neighbor.first;
            int weight = neighbor.second;
            int distance = current_distance + weight;

            if (distance < distances[neighbor_vertex])
            {
                distances[neighbor_vertex] = distance;
                pq.push({distance, neighbor_vertex});
            }
        }
    }

    return 0;
}

int main()
{
    cin >> t;

    for (int q = 0; q < t; q++)
    {
        cin >> N >> M;
        for (int i = 0; i < N; i++)
        {
            graph[i].clear();
        }

        for (int i = 0; i < M; i++)
        {
            int u, v, w;
            cin >> u >> v >> w;
            graph[u - 1].push_back({v - 1, w});
            graph[v - 1].push_back({u - 1, w});
        }

        cin >> D;

        dijkstra(D - 1);

        for (int i = 0; i < N; i++)
        {
            if (D - 1 == i)
                continue;
            if (distances[i] == INT_MAX)
                cout << -1 << " ";
            else
                cout << distances[i] << " ";
        }

        cout << endl;
    }

    return 0;
}