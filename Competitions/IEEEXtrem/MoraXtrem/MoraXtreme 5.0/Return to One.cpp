#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int t, a, b;

int getCount(int n, int c)
{

    if (n == 1)
        return c;

    if (n % 2 == 0)
        return getCount(n / 2, c + 1);

    return getCount(n * 3 + 1, c + 1);
}

int main()
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */

    cin >> t;

    for (int i = 0; i < t; i++)
    {
        cin >> a >> b;

        a = getCount(a, 0);
        b = getCount(b, 0);

        if (a > b)
            cout << "Kalpa" << endl;
        else if (a == b)
            cout << "-" << endl;
        else
            cout << "Kapila" << endl;
    }

    return 0;
}
