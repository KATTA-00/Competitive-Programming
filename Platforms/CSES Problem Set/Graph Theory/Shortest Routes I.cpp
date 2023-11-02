#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;
#define MAX 100001

typedef pair<long long, int> pii;
vector<pii> graph[MAX];
long long distances[MAX];

void dijkstra(int start, int N)
{
    fill(distances, distances + N, LONG_LONG_MAX);
    distances[start] = 0;
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    pq.push({0, start});

    while (!pq.empty())
    {
        long long current_distance = pq.top().first;
        int current_vertex = pq.top().second;
        pq.pop();

        if (current_distance > distances[current_vertex])
        {
            continue;
        }

        for (auto neighbor : graph[current_vertex])
        {
            int neighbor_vertex = neighbor.first;
            long weight = neighbor.second;
            long long distance = current_distance + weight;

            if (distance < distances[neighbor_vertex])
            {
                distances[neighbor_vertex] = distance;
                pq.push({distance, neighbor_vertex});
            }
        }
    }
}

int main()
{
    int t;
    t = 1;
    while (t--)
    {
        int N, M;
        cin >> N >> M;

        for (int i = 0; i < N; i++)
        {
            graph[i].clear(); // Clear the graph for each test case
        }

        for (int i = 0; i < M; i++)
        {
            int u, v, w;
            cin >> u >> v >> w;
            graph[u - 1].push_back({v - 1, w});
        }

        dijkstra(0, N);

        for (int j = 0; j < N; j++)
        {
            cout << (distances[j] == LONG_LONG_MAX ? -1 : distances[j]) << " ";
        }
        cout << endl;
    }

    return 0;
}
