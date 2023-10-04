#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;
const int maxN = 2e5;

int N, p, x[maxN + 1], t;
tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> T;

int main()
{
    cin >> N;
    for (int i = 1; i <= N; i++)
    {
        cin >> t;
        x[i] = t;
        T.insert(i);
    }

    for (int i = 0; i < N; i++)
    {
        cin >> p;
        cout << x[*T.find_by_order(p - 1)] << " ";
        T.erase(T.find_by_order(p - 1));
    }
}