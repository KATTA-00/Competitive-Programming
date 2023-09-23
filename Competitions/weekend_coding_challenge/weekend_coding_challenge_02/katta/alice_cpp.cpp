#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

typedef pair<int, int> pii;

int dijkstra(vector<vector<pii>> &graph, int start, int end)
{
    int n = graph.size();
    vector<int> distances(n, INT_MAX);
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

    return distances[end];
}

int main()
{
    int N, M, D, Q;
    cin >> N >> M;
    vector<vector<pii>> graph(N);

    for (int i = 0; i < M; i++)
    {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u - 1].push_back({v - 1, w});
    }

    cin >> D >> Q;
    vector<int> cities(Q);

    for (int i = 0; i < Q; i++)
    {
        cin >> cities[i];
    }

    for (int city : cities)
    {
        int distance = dijkstra(graph, city - 1, D - 1);
        if (distance == INT_MAX)
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