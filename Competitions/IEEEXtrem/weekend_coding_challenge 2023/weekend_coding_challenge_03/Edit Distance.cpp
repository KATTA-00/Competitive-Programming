#include <bits/stdc++.h>

using namespace std;

string str1, str2;

int main()
{
    cin >> str1;
    cin >> str2;

    vector<vector<int>> dp(str1.size() + 1, vector<int>(str2.size() + 1, INT32_MAX));
    dp[0][0] = 0;

    for (int i = 0; i <= str1.size(); i++)
    {
        for (int j = 0; j <= str2.size(); j++)
        {

            if (i != 0)
            {

                dp[i][j] = std::min(dp[i][j], dp[i - 1][j] + 1);
            }
            if (j != 0)
            {
                dp[i][j] = std::min(dp[i][j], dp[i][j - 1] + 1);
            }

            if (i != 0 && j != 0)
            {
                int new_cost = dp[i - 1][j - 1] + (str1[i - 1] != str2[j - 1]);
                dp[i][j] = std::min(dp[i][j], new_cost);
            }
        }
    }

    cout << dp[str1.size()][str2.size()] << endl;

    return 0;
}
