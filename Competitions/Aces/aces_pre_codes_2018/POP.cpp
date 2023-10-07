#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int n;
char ch;
int p = 0;
int o = 0;

int main()
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> ch;
        if (ch == 'P')
            p++;
        if (ch == 'O')
            o++;
    }

    if (o * 2 <= p)
        cout << o;
    else
        cout << p / 2;

    return 0;
}
