#include <bits/stdc++.h>

using namespace std;
const int MAX = 2e5 + 1;

int h, c, ans;
int cc;
int hotel[MAX];
// lo and hi contains the limits of the maximum value in i position
// mx - maximum value (segment tree values)
// mp - mapping
int lo[4 * MAX], hi[4 * MAX], mx[4 * MAX], mp[MAX];

void pull(int i)
{
    mx[i] = (hotel[mx[2 * i]] >= hotel[mx[2 * i + 1]] ? mx[2 * i] : mx[2 * i + 1]);
}

void init(int i, int l, int r)
{
    lo[i] = l;
    hi[i] = r;
    if (l == r)
    {
        mp[l] = i;
        mx[i] = l;
        return;
    }
    int m = l + (r - l) / 2;
    init(2 * i, l, m);
    init(2 * i + 1, m + 1, r);
    pull(i);
}

void update(int i, int v)
{
    hotel[i] -= v;
    i = mp[i];
    i >>= 1;
    while (i > 0)
    {
        pull(i);
        i >>= 1;
    }
}

int find(int i, int v)
{
    if (lo[i] == hi[i])
        return lo[i];

    return (hotel[mx[2 * i]] >= v ? find(2 * i, v) : find(2 * i + 1, v));
}

int main()
{
    cin >> h >> c;

    for (int i = 1; i <= h; i++)
    {
        cin >> cc;
        hotel[i] = cc;
    }

    init(1, 1, h);

    for (int i = 0; i < c; i++)
    {
        cin >> cc;
        ans = hotel[mx[1]] < cc ? 0 : find(1, cc);
        if (ans)
            update(ans, cc);
        cout << ans << " ";
    }
    cout << endl;

    return 0;
}