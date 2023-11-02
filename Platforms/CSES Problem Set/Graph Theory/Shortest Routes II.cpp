#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;
#define MAX 5005

typedef pair<int, int> pii;
vector<pii> graph[MAX];
int N, M, D, Q, B;
int distances[MAX];

int dijkstra(int start, int end)
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

    return distances[end];
}

int main()
{
    cin >> N >> M >> Q;

    for (int i = 0; i < M; i++)
    {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u - 1].push_back({v - 1, w});
        graph[v - 1].push_back({u - 1, w});
    }

    for (int i = 0; i < Q; i++)
    {
        cin >> D >> B;

        int distance = dijkstra(D - 1, B - 1);

        if (distance == INT_MAX)
        {
            cout << "-1" << endl;
        }
        else
        {
            cout << distance << endl;
        }
    }

    return 0;
}