#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define INF 10000

int main()
{

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int v, e;
    scanf("%d %d", &v, &e);

    int m[v][v];
    for (int i = 0; i < v; i++)
    {
        for (int j = 0; j < v; j++)
        {
            if (i == j)
                m[i][j] = 0;
            else
                m[i][j] = INF;
        }
    }

    int a, b, c;
    for (int i = 0; i < e; i++)
    {
        scanf("%d %d %d", &a, &b, &c);
        m[a - 1][b - 1] = c;
    }

    for (int k = 0; k < v; k++)
    {
        for (int i = 0; i < v; i++)
        {
            for (int j = 0; j < v; j++)
            {
                if (m[i][k] + m[k][j] < m[i][j])
                    m[i][j] = m[i][k] + m[k][j];
            }
        }
    }

    int num;
    scanf("%d", &num);
    for (int i = 0; i < num; i++)
    {
        scanf("%d %d", &a, &b);
        if (m[a - 1][b - 1] == INF)
            printf("-1\n");
        else
            printf("%d\n", m[a - 1][b - 1]);
    }

    return 0;
}