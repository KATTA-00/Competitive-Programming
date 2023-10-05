#include <bits/stdc++.h>
using namespace std;

#define Max 100005

int UniqDif(int n, int a[])
{

    bitset<Max> bset;
    bitset<Max> diff;

    // Traverse the array, arr[]
    for (int i = 0; i < n; i++)
    {

        // Add in bitset
        bset.set(a[i]);
    }

    for (int i = 0; i <= Max; i++)
    {

        // If i-th bit is set
        if (bset[i])
        {
            diff = diff | (bset >> i);
        }
    }

    int X = bset.count();
    int c = 0;
    for (int i = 1; i <= Max; i++)
    {

        if (diff[i])
        {
            c++;
        }
    }

    return c;
}

int main()
{
    int num;
    cin >> num;
    int a[num];

    for (int i = 0; i < num; i++)
    {
        cin >> a[i];
    }

    cout << UniqDif(num, a);

    return 0;
}
