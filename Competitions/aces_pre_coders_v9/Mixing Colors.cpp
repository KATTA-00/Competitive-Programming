#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

int n, k;
int temp;
int first, second;
priority_queue<int, vector<int>, greater<int>> pq;

int main()
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    cin >> n >> k;

    if (n < 2)
    {
        cout << -1;
        return 0;
    }

    for (int i = 0; i < n; i++)
    {
        cin >> temp;
        pq.push(temp);
    }

    int count = 0;
    first = pq.top();
    while (first < k)
    {

        if (pq.size() < 2)
        {
            cout << -1;
            return 0;
        }

        pq.pop();
        second = pq.top();
        pq.pop();
        count++;

        pq.push(first + 2 * second);
        first = pq.top();
    }

    cout << count;

    return 0;
}
