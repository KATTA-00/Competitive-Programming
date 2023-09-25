#include <iostream>
#include <vector>
#include <queue>
#include <limits>
#include <unordered_set>

using namespace std;

const int INF = numeric_limits<int>::max();
const int MAX_N = 100010;

vector<pair<int, int>> adj[MAX_N];
vector<vector<int>> currencies(MAX_N);
int dist[MAX_N][11]; // Minimum times to reach each planet with specific currencies

struct State {
    int planet, currency, time;

    State(int p, int c, int t) : planet(p), currency(c), time(t) {}

    bool operator>(const State& other) const {
        return time > other.time;
    }
};

int main() {
    int N, M, K;
    cin >> N >> M >> K;

    for (int i = 1; i <= N; ++i) {
        int num_currencies;
        cin >> num_currencies;
        currencies[i].resize(num_currencies);
        for (int j = 0; j < num_currencies; ++j) {
            cin >> currencies[i][j];
        }
    }

    for (int i = 0; i < M; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].emplace_back(v, w);
        adj[v].emplace_back(u, w);
    }

    for (int i = 1; i <= N; ++i) {
        for (int j = 0; j <= K; ++j) {
            dist[i][j] = INF;
        }
    }

    priority_queue<State, vector<State>, greater<State>> pq;
    pq.emplace(1, 0, 0); // Start at planet 1 with currency 0
    dist[1][0] = 0;

    while (!pq.empty()) {
        State current = pq.top();
        pq.pop();

        int planet = current.planet;
        int currency = current.currency;
        int time = current.time;

        if (time > dist[planet][currency]) {
            continue; // Skip outdated information
        }

        for (const auto& edge : adj[planet]) {
            int neighbor = edge.first;
            int travel_time = edge.second;

            int new_time = time + travel_time;
            int new_currency = currency;

            // Check if the planet has the currency needed
            unordered_set<int> currencies_set(currencies[neighbor].begin(), currencies[neighbor].end());
            if (currencies_set.count(currency) == 0) {
                new_currency++;
            }

            // Relaxation step
            if (new_time < dist[neighbor][new_currency] && new_currency <= K) {
                dist[neighbor][new_currency] = new_time;
                pq.emplace(neighbor, new_currency, new_time);
            }
        }
    }

    int min_time = INF;
    for (int i = 0; i <= K; ++i) {
        min_time = min(min_time, dist[N][i]);
    }

    cout << min_time << endl;

    return 0;
}
