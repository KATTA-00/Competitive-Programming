#include <iostream>
#include <vector>
using namespace std;

int main() {
    const long long MOD = 1000000007;

    int n;
    cin >> n;

    vector<string> grid(n);
    for (int i = 0; i < n; i++) {
        cin >> grid[i];
    }

    vector<vector<long long>> paths(n + 1, vector<long long>(n + 1, 0));
    paths[0][0] = 1;

    for (int row = 0; row < n; row++) {
        for (int col = 0; col < n; col++) {
            if (grid[row][col] != '*') {
                if (row > 0) {
                    paths[row][col] += paths[row - 1][col];
                    paths[row][col] %= MOD;
                }
                if (col > 0) {
                    paths[row][col] += paths[row][col - 1];
                    paths[row][col] %= MOD;
                }
            } else {
                paths[row][col] = 0;
            }
        }
    }

    cout << (n > 0 ? paths[n - 1][n - 1] % MOD : -1) << endl;

    return 0;
}


