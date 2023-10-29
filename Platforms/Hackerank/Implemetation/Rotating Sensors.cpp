#include <iostream>
#include <vector>

using namespace std;

void matrixRotation(vector<vector<int>> &matrix, int r)
{
    int m = matrix[0].size();
    int n = matrix.size();

    int g = min(m, n) / 2;

    for (int p = 0; p < g; ++p)
    {
        vector<int> new_matrix;

        for (int j = p; j < m - p; ++j)
        {
            new_matrix.push_back(matrix[p][j]);
        }

        for (int i = p + 1; i < n - p; ++i)
        {
            new_matrix.push_back(matrix[i][m - 1 - p]);
        }

        for (int j = m - p - 2; j >= p; --j)
        {
            new_matrix.push_back(matrix[n - 1 - p][j]);
        }

        for (int i = n - 2 - p; i > p; --i)
        {
            new_matrix.push_back(matrix[i][p]);
        }

        int num_r = r % new_matrix.size();

        vector<int> temp(new_matrix.begin() + num_r, new_matrix.end());
        temp.insert(temp.end(), new_matrix.begin(), new_matrix.begin() + num_r);

        int index = 0;
        for (int j = p; j < m - p; ++j)
        {
            matrix[p][j] = temp[index++];
        }

        for (int i = p + 1; i < n - p; ++i)
        {
            matrix[i][m - 1 - p] = temp[index++];
        }

        for (int j = m - p - 2; j >= p; --j)
        {
            matrix[n - 1 - p][j] = temp[index++];
        }

        for (int i = n - 2 - p; i > p; --i)
        {
            matrix[i][p] = temp[index++];
        }
    }

    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < m; ++j)
        {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{
    int m, n, r;
    cin >> m >> n >> r;
    vector<vector<int>> matrix(m, vector<int>(n));

    for (int i = 0; i < m; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            cin >> matrix[i][j];
        }
    }

    matrixRotation(matrix, r);

    return 0;
}
