#include <bits/stdc++.h>
using namespace std;

#define MAX_NUM 1001
int n, m;
char grid[MAX_NUM][MAX_NUM];
int monsterGrid[MAX_NUM][MAX_NUM];
int humanGrid[MAX_NUM][MAX_NUM];
bool visited[MAX_NUM][MAX_NUM];
pair<int, int> start;
pair<int, int> finish;

int x_axis[4] = {1, -1, 0, 0};
int y_axis[4] = {0, 0, 1, -1};

bool checkValid(int i, int j)
{
    if (grid[i][j] == '#')
        return false;
    else if (i >= n || j >= m || i < 0 || j < 0)
        return false;

    return true;
}

int main()
{
    cin >> n >> m;

    queue<pair<int, int>> q;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
        {
            cin >> grid[i][j];

            monsterGrid[i][j] = MAX_NUM;
            visited[i][j] = false;
            if (grid[i][j] == 'M')
            {
                q.push(make_pair(i, j));
                monsterGrid[i][j] = 0;
            }
            else if (grid[i][j] == 'A')
            {
                start = make_pair(i, j);
                humanGrid[i][j] = 0;
            }
        }

    // q.push(monster.front());
    // monster.pop();

    while (!q.empty())
    {
        pair<int, int> node = q.front();
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int x = node.first + x_axis[i];
            int y = node.second + y_axis[i];

            if (checkValid(x, y) && monsterGrid[x][y] > monsterGrid[node.first][node.second] + 1)
            {
                monsterGrid[x][y] = monsterGrid[node.first][node.second] + 1;
                q.push(make_pair(x, y));
            }
        }
    }

    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < m; j++)
    //     {
    //         cout << monsterGrid[i][j] << "\t";
    //     }
    //     cout << endl;
    // }

    q.empty();
    q.push(start);
    visited[start.first][start.second] = true;
    int x, y;
    bool flag = false;

    if (start.first == 0 || start.second == 0 || start.first == n - 1 || start.second == m - 1)
    {
        flag = true;
        finish = start;
    }
    while (!q.empty() && !flag)
    {
        pair<int, int> node = q.front();
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            x = node.first + x_axis[i];
            y = node.second + y_axis[i];

            if (checkValid(x, y) && !visited[x][y] && monsterGrid[x][y] > humanGrid[node.first][node.second] + 1)
            {
                humanGrid[x][y] = humanGrid[node.first][node.second] + 1;
                visited[x][y] = true;
                q.push(make_pair(x, y));

                if (x == 0 || y == 0 || x == n - 1 || y == m - 1)
                {
                    flag = true;
                    finish = make_pair(x, y);
                    break;
                }
            }
        }

        if (flag)
            break;
    }

    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < m; j++)
    //     {
    //         cout << humanGrid[i][j] << "\t";
    //     }
    //     cout << endl;
    // }

    if (!flag)
    {
        cout << "NO" << endl;
        return 0;
    }

    cout << "YES" << endl;
    cout << humanGrid[finish.first][finish.second] << endl;

    vector<char> path;
    char c;
    c = grid[finish.first][finish.second];

    while (c != 'A')
    {
        // cout << finish.first << " " << finish.second << endl;

        for (int i = 0; i < 4; i++)
        {
            x = finish.first + x_axis[i];
            y = finish.second + y_axis[i];

            if (checkValid(x, y) && humanGrid[x][y] + 1 == humanGrid[finish.first][finish.second] && visited[x][y])
            {
                finish = make_pair(x, y);
                c = grid[x][y];

                if (i == 0)
                    path.push_back('U');
                if (i == 1)
                    path.push_back('D');
                if (i == 2)
                    path.push_back('L');
                if (i == 3)
                    path.push_back('R');

                break;
            }
        }
    }

    reverse(path.begin(), path.end());

    for (char elemet : path)
    {
        cout << elemet;
    }

    cout << endl;

    return 0;
}