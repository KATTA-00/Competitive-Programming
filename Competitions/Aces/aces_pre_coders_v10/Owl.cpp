#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define MAX 100001
int link[MAX];
int size[MAX];
int numbers[MAX];
vector<int> components;

// store the representative of each node

int find(int x)
{
    while (x != link[x])
        x = link[x];
    return x;
}

bool same(int a, int b)
{
    return find(a) == find(b);
}

void unite(int a, int b)
{
    a = find(a);
    b = find(b);

    if (size[a] < size[b])
        swap(a, b);

    size[a] += size[b];
    link[b] = a;
}

int n, m, t;

int main()
{
    for (int i = 1; i <= n; i++)
        link[i] = i;
    for (int i = 1; i <= n; i++)
        size[i] = 1;

    cin >> n >> m >> t;
    int x, a, b;

    int c = 0;
    for (int i = 0; i < m; i++)
    {
        cin >> x >> a >> b;

        if (!same(a, b))
        {

            

            if (find(a) == a && find(b) == b){
                numbers[a] = c;
                numbers[b] = c;
                c++;
            }else{
                
                numbers[a] = numbers[find(a)];
            }

            unite(a, b);
        }
    }

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    return 0;
}