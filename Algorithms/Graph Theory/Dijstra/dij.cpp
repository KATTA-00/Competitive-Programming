#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;
#define MAX 3001

typedef pair<int, int> pii;
vector<pii> graph[MAX];
int distances[MAX];

void dijkstra(int start, int N)
{
    fill(distances, distances + N, INT_MAX);
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
}

int main()
{
    int t;
    cin >> t;
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
            graph[v - 1].push_back({u - 1, w});
        }

        int c;
        cin >> c;

        dijkstra(c - 1, N);

        for (int j = 0; j < N; j++)
        {
            if (c != j + 1)
                cout << (distances[j] == INT_MAX ? -1 : distances[j]) << " ";
        }
        cout << endl;
    }

    return 0;
}
