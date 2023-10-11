#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
const int maxN = 40;

int N, t[maxN];
ll x, sum, cnt;
unordered_map<ll, int> freq;

int main()
{
    cin >> N >> x;
    for (int i = 0; i < N; i++)
        cin >> t[i];

    sort(t, t + N);

    if (N == 1)
    {
        cout << ((x == t[0]) ? 1 : 0) << endl;
        return 0;
    }

    freq.reserve(1 << (N / 2 - 1));

    for (int i = 0; i < (1 << (N / 2 - 1)); i++)
    {
        sum = 0;
        for (int j = 0; j < N / 2 - 1; j++)
            if (i & (1 << j))
                sum += t[j];
        freq[sum]++;
    }

    for (int i = 0; i < (1 << ((N + 1) / 2 + 1)); i++)
    {
        sum = 0;
        for (int j = 0; j < (N + 1) / 2 + 1; j++)
            if (i & (1 << j))
                sum += t[N / 2 - 1 + j];
        if (freq.find(x - sum) != freq.end())
            cnt += freq[x - sum];
    }

    cout << cnt << endl;
}