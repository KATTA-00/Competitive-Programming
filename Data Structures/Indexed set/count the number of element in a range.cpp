#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;
typedef pair<int, int> pii;
const int maxN = 2e5;

char c;
int N, Q, a, b, p[maxN + 1], temp;
tree<pii, null_type, less<pii>, rb_tree_tag, tree_order_statistics_node_update> T;

int main()
{
    cin >> N >> Q;
    for (int i = 1; i <= N; i++)
    {
        cin >> temp;
        p[i] = temp;
        T.insert({temp, i});
    }

    for (int i = 0; i < Q; i++)
    {
        cin >> c >> a >> b;
        if (c == '!')
        {
            T.erase({p[a], a});
            T.insert({b, a});
            p[a] = b;
        }
        else if (c == '?')
        {
            cout << T.order_of_key({b + 1, 0}) - T.order_of_key({a, 0}) << endl;
        }
    }
}