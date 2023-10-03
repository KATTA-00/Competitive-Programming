#include <bits/stdc++.h>
using namespace std;

unsigned long long arr[20];
int n;

int head[64];
int size[64];
int total_size = 64;

long long ans = 0;

int find(int n)
{
    if (head[n] == n)
        return n;
    return find(head[n]);
}

void connect(int a, int b)
{
    int fa = find(a);
    int fb = find(b);
    if (fa == fb)
        return;

    if (size[fa] > size[fb])
        swap(fa, fb);
    size[fb] += size[fa];
    head[fa] = fb;
    total_size--;
}

void rec(int pos)
{
    if (pos == n)
    {
        ans += total_size;
        return;
    }

    rec(pos + 1);

    int nhead[64];
    int nsize[64];
    int ntotal_size = total_size;
    for (int i = 0; i < 64; i++)
        nhead[i] = head[i], nsize[i] = size[i];

    int ipos = -1;
    for (int i = 0; i < 64; i++)
        if (arr[pos] & (1ull << i))
        {
            ipos = i;
            break;
        }
    for (int i = ipos + 1; i < 64; i++)
        if (arr[pos] & (1ull << i))
            connect(i, ipos);

    rec(pos + 1);
    for (int i = 0; i < 64; i++)
        head[i] = nhead[i], size[i] = nsize[i];
    total_size = ntotal_size;
}

int main()
{
    cin >> n;

    for (int i = 0; i < n; i++)
        cin >> arr[i];

    for (int i = 0; i < 64; i++)
        head[i] = i, size[i] = 1;
    total_size = 64;

    rec(0);
    cout << ans << endl;
}
