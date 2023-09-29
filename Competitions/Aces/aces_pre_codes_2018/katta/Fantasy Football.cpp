#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int n, u, c, s;

int main()
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    cin >> n >> u >> c >> s;

    int can = u / c;

    int upgrade;

    if (n > can)
        upgrade = can;
    else
    {
        cout << n;
        return 0;
    }

    int rem = n - upgrade;

    int buy = 0;
    int money = 0;
    int i = 1;

    if (rem == 1)
    {
        cout << upgrade;
        return 0;
    }

    for (i = 1; i <= rem; i++)
    {

        if (money >= c)
        {
            money -= c;
            continue;
        }

        buy = 0;
        for (int j = 1; j <= rem - i; j++)
        {
            money += s;
            buy++;
            if (money >= c)
            {
                break;
            }
        }

        rem = rem - buy;
        rem--;
        money -= c;
    }

    cout << i - 1 + upgrade << endl;

    return 0;
}
