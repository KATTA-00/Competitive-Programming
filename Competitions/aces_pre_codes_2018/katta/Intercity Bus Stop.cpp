#include <bits/stdc++.h>

using namespace std;

int main()
{
    long t;
    cin >> t;
    for (int a_0 = 0; a_0 < t; a_0++)
    {
        long n, k;
        cin >> n >> k;

        long position = k;
        long line = 0;
        bool cangetin = 0;
        bool nocheck = 0;

        for (int i = 0; i < n; i++)
        {
            long c, w;
            cin >> c >> w;
            if (nocheck == 1)
            {
                continue;
            }
            line = line + w;
            if (position <= line)
            {
                cangetin = 1;
            }
            else
            {
                line = line - w + c;
                if (position <= line)
                {
                    position = line + 1;
                }
            }
        }
        if (cangetin == 1)
        {
            if (position == k)
            {
                cout << 0 << endl;
            }
            else
            {
                cout << position - k << endl;
            }
        }
        else
        {
            cout << -1 << endl;
        }
    }
    return 0;
}