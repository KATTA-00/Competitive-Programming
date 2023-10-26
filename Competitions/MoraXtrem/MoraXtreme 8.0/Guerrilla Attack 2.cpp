#include <bits/stdc++.h>
using namespace std;

const int N = 501;
long long n, m, Assigned[N],K;
long long Visited[N], t=0;
vector<int> a[N];
long long dx[N], dy[N], cx[N], cy[N];
bool visit(int u) {
    if (Visited[u]!=t)
        Visited[u]=t;
    else
        return false;

    for (int i=0; int v=a[u][i]; i++)
    if (!Assigned[v] || visit(Assigned[v])) {
        Assigned[v]=u;
        return true;
    }
     return false;
}
long long distance(int i, int j) {
    return (long long) (cx[i] - dx[j]) * (cx[i] - dx[j]) + (cy[i] - dy[j]) * (cy[i] - dy[j]);
}
bool count(long long mid) {
    for (int i = 1; i <= m + n; i++) {
        a[i].clear();
        Assigned[i] = 0;
        Visited[i] = 0;
    }
    
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            if (distance(i, j) <= mid)  a[i].push_back(j + n);
    
    for (int i = 1; i <= n; i++) a[i].push_back(0);
    int Count = 0;
    for (int i = 1; i <= n; i++) {
        t++;
        Count += visit(i);
    }
    
    if (Count >= K) return true;
    return false;
}
int main() {
    cin >> n >> m >> K;
    for (int i = 1; i <= n; i++) cin >> cx[i] >> cy[i];
    for (int i = 1; i <= m; i++) cin >> dx[i] >> dy[i];
    long long l = 0, r = pow(10,14);
    while (l < r) {
        long long mid = (l + r) / 2;
        if (count(mid)) r = mid;
        else l = mid + 1;
    }
    cout << l << endl;
}
