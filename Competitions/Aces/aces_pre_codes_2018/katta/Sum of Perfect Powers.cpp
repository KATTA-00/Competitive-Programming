#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>
using namespace std;

int n, m;

int getDivide(int n, int m)
{
    int count = 0;
    while (n > 0)
    {
        n -= m;
        count++;
    }

    return count;
}

int main()
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    cin >> n >> m;
    int c;
    vector<int> k;
    map<int, int> myMap;

    for (int i = 0; i < n; i++)
    {
        cin >> c;
        k.push_back(c);
    }

    sort(k.begin(), k.end());

    for (int i = 0; i < n; i++)
    {
        myMap[k[i]] = 0;
    }

    for (int i = 0; i < n; i++)
    {
        myMap[k[i]]++;
    }

    map<int, int> myMap_c(myMap);
    for (auto u : myMap)
    {
        int div = getDivide(u.second, m);
        if (div != 0)
        {
            myMap_c[u.first + div] = (u.second / (div * m)) + myMap_c[u.first + div];
            myMap_c.erase(u.first);
        }
    }

    // for (auto u : myMap_c)
    // {
    //     cout << " " << u.first << " " << u.second << endl;
    // }

    string output = "";
    for (int i = 0; i <= myMap_c.rbegin()->first; i++)
    {
        // cout << myMap_c[i] << endl;
        output += (myMap_c[i] < 10) ? to_string(myMap_c[i]) : string(1, (char)('a' + i - 9));
    }

    reverse(output.begin(), output.end());
    cout << output << endl;

    return 0;
}
