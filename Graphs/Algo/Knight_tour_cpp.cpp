// C++ program for Knight Tour problem
#include <bits/stdc++.h>
using namespace std;

#define N 7
#define MAX 9999
int sol[MAX][MAX];
int xMove[8] = {2, 1, -1, -2, -2, -1, 1, 2};
int yMove[8] = {1, 2, 2, 1, -1, -2, -2, -1};

int solveKTUtil(int x, int y, int movei);

int isSafe(int x, int y)
{
    return (x >= 0 && x < N && y >= 0 && y < N && sol[x][y] == -1);
}

void printSolution()
{
    for (int x = 0; x < N; x++)
    {
        for (int y = 0; y < N; y++)
            cout << " " << setw(2) << sol[x][y] << " ";
        cout << endl;
    }
}

int solveKT()
{

    /* Initialization of solution matrix */
    for (int x = 0; x < N; x++)
        for (int y = 0; y < N; y++)
            sol[x][y] = -1;

    // Since the Knight is initially at the first block
    sol[0][0] = 0;

    /* Start from 0,0 and explore all tours using
    solveKTUtil() */
    if (solveKTUtil(0, 0, 1) == 0)
    {
        cout << "Solution does not exist";
        return 0;
    }
    else
        printSolution();

    return 1;
}

/* A recursive utility function to solve Knight Tour
problem */
int solveKTUtil(int x, int y, int movei)
{
    int k, next_x, next_y;

    if (movei == N * N)
        return 1;

    for (k = 0; k < 8; k++)
    {
        next_x = x + xMove[k];
        next_y = y + yMove[k];
        if (isSafe(next_x, next_y))
        {
            sol[next_x][next_y] = movei;
            if (solveKTUtil(next_x, next_y, movei + 1) == 1)
                return 1;
            else
                // backtracking
                sol[next_x][next_y] = -1;
        }
    }

    return 0;
}

// Driver Code
int main()
{
    // Function Call
    solveKT();
    return 0;
}

// This code is contributed by ShubhamCoder
