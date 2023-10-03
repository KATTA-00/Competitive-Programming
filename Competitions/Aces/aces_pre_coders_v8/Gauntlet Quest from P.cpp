#include <bits/stdc++.h>
using namespace std;
using ll = int64_t;
using vecl = vector<ll>;
using pll = pair<ll, ll>;
using vecpl = vector<pll>;
using mapl = unordered_map<ll, vecl>;
using vecvecl = vector<vecl>;
using graph_t = vector<vecpl>;

ll solve(vecl &stones, graph_t &graph, ll n, ll k)
{
    ll distances[n][1 << k];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < (1 << k); j++)
        {
            distances[i][j] = LONG_LONG_MAX;
        }
    }

    auto heap = priority_queue<tuple<ll, ll, ll>>();

    ll target_node = n - 1;
    ll target_stone = (1 << k) - 1;
    ll dis = 0;
    ll node = 0;
    ll stone = stones[0];

    heap.push(make_tuple(-dis, node, stone));

    while (1)
    {
        tuple<ll, ll, ll> state = heap.top();

        ll dis = -get<0>(state);
        ll node = get<1>(state);
        ll stone = get<2>(state);

        // cout << dis << " " << node << " " << stone << endl;
        heap.pop();

        if (dis >= distances[node][stone])
            continue;

        distances[node][stone] = dis;

        if (node == target_node && stone == target_stone)
        {
            break;
        }

        for (auto c : graph[node])
        {
            ll new_dis = dis + c.second;
            ll new_stone = stones[c.first] | stone;

            if (new_dis >= distances[c.first][new_stone])
                continue;

            heap.push(make_tuple(-new_dis, c.first, new_stone));
        }
    }

    ll ans = LONG_LONG_MAX;
    for (int i = 0; i <= target_stone; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            ll s = i | j;

            if (s != target_stone)
                continue;
            
            ans = min(ans, max(distances[target_node][i], distances[target_node][j]));
        }
    }
    return ans;
}

int main()
{
    int n, m, k;
    cin >> n >> m >> k;
    vecl stones = vecl(n);
    graph_t graph = graph_t(n);

    for (int i = 0; i < n; i++)
    {
        int nc;
        cin >> nc;
        int c;
        for (int j = 0; j < nc; j++)
        {
            cin >> c;
            c--;
            stones[i] |= (1 << c);
        }
    }

    for (int i = 0; i < m; i++)
    {
        ll t, u, v;
        cin >> u >> v >> t;
        u--;
        v--;
        graph[u].push_back(make_pair(v, t));
        graph[v].push_back(make_pair(u, t));
    }

    cout << solve(stones, graph, n, k) << endl;
    return 0;
}