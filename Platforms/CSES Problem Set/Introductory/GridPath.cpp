
//  backtracking, dynamic programming

#include <iostream>
using namespace std;

const int n = 7;
bool visited[n][n];
int directions[49];

void findPaths(int r, int c, int &count, int steps) {
    if (r == n - 1 && c == 0) {
        count += (steps == n * n - 1);
        return;
    }

    if (((r + 1 == n || (visited[r - 1][c] && visited[r + 1][c])) && c - 1 >= 0 && c + 1 < n && !visited[r][c - 1] && !visited[r][c + 1]) ||
        ((c + 1 == n || (visited[r][c - 1] && visited[r][c + 1])) && r - 1 >= 0 && r + 1 < n && !visited[r - 1][c] && !visited[r + 1][c]) ||
        ((r == 0 || (visited[r + 1][c] && visited[r - 1][c])) && c - 1 >= 0 && c + 1 < n && !visited[r][c - 1] && !visited[r][c + 1]) ||
        ((c == 0 || (visited[r][c + 1] && visited[r][c - 1])) && r - 1 >= 0 && r + 1 < n && !visited[r - 1][c] && !visited[r + 1][c])) {
        return;
    }

    visited[r][c] = true;

    if (directions[steps] != -1) {
        int nextR = r, nextC = c;
        switch (directions[steps]) {
            case 0: nextR = r - 1; break;
            case 1: nextC = c + 1; break;
            case 2: nextR = r + 1; break;
            case 3: nextC = c - 1; break;
        }
        if (nextR >= 0 && nextR < n && nextC >= 0 && nextC < n && !visited[nextR][nextC]) {
            findPaths(nextR, nextC, count, steps + 1);
        }
        visited[r][c] = false;
        return;
    }

    int dr[] = {1, 0, -1, 0};
    int dc[] = {0, 1, 0, -1};
    for (int i = 0; i < 4; i++) {
        int nextR = r + dr[i];
        int nextC = c + dc[i];
        if (nextR >= 0 && nextR < n && nextC >= 0 && nextC < n && !visited[nextR][nextC]) {
            findPaths(nextR, nextC, count, steps + 1);
        }
    }

    visited[r][c] = false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string path;
    cin >> path;

    for (int i = 0; i < path.length(); i++) {
        if (path[i] == '?') {
            directions[i] = -1;
        } else if (path[i] == 'U') {
            directions[i] = 0;
        } else if (path[i] == 'R') {
            directions[i] = 1;
        } else if (path[i] == 'D') {
            directions[i] = 2;
        } else if (path[i] == 'L') {
            directions[i] = 3;
        }
    }

    int count = 0;
    findPaths(0, 0, count, 0);
    cout << count << endl;

    return 0;
}
