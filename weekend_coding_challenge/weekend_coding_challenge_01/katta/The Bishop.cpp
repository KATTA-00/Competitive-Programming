#include <bits/stdc++.h>

using namespace std;

#define MAX_NUM 9

int n = 8, m = 8;
queue<pair<int, int>> q;
bool visited[MAX_NUM][MAX_NUM];
int dist = 0;

int neighborX[4] = {1, 1, -1, -1};
int neighborY[4] = {1, -1, 1, -1};
pair<int, int> previosNode[MAX_NUM][MAX_NUM];

bool isValid(int y, int x)
{
    if (y < 1)
        return false;
    if (x < 1)
        return false;
    if (y > n)
        return false;
    if (x > m)
        return false;
    return true;
}

int main()
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int a, b, k, l;
    cin >> a >> b >> k >> l;

    pair<int, int> new_cc{a, b};
    q.push(new_cc);
    visited[a][b] = true;

    int x;
    int y;
    bool flag = false;
    while (!q.empty())
    {
        pair<int, int> cc = q.front();
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            x = cc.first + neighborX[i];
            y = cc.second + neighborY[i];

            if (visited[x][y] || !isValid(x, y))
                continue;

            visited[x][y] = true;

            previosNode[x][y] = make_pair(cc.first, cc.second);

            if (x == k && y == l)
            {
                flag = true;
                break;
            }

            pair<int, int> new_cc{x, y};
            q.push(new_cc);
        }

        if (flag)
            break;
    }

    if (flag)
    {

        while (!(x == a && y == b))
        {
            // cout << previosNode[x][y].first << " " << previosNode[x][y].second << endl;
            dist++;
            int temp = x;
            x = previosNode[x][y].first;
            y = previosNode[temp][y].second;
        }

        cout << dist / 3 << endl;
    }
    else
        cout << -1 << endl;

    return 0;
}
