#include <bits/stdc++.h>
using namespace std;
using ll = int64_t;
using vecl = vector<ll>;
using pll = pair<ll, ll>;
using vecpl = vector<pll>;
using mapl = unordered_map<ll, vecl>;
using mapsl = unordered_map<string, ll>;
using mapls = unordered_map<ll, string>;
using vecvecl = vector<vecl>;

void dfs(mapl &t, int s, vecl &stack, vecl &v, vecl &l, vecl &p, ll cl = 0)
{
    if (v[s])
    {
        return;
    }
    v[s] = 1;
    l[s] = cl;
    for (auto x : t[s])
    {

        if (!v[x])
        {
            p[x] = s;
            dfs(t, x, stack, v, l, p, cl + 1);
        }
    }
    stack.push_back(s);
}

struct Tree_Climb
{
    vecvecl climb_arr;
    vecl l;
    vecl parents;
    int max_len = 0;
    Tree_Climb(mapl &tree, int n, ll root)
    {
        parents = vecl(n, -1);
        climb_arr = vecvecl(n);
        max_len = 2 * log2(n) + 3;
        for (int i = 0; i < n; i++)
        {
            climb_arr[i] = vecl(max_len, -1);
        }
        vecl ds = vecl();
        vecl v = vecl(n, 0);
        l = vecl(n, 0);
        dfs(tree, root, ds, v, l, parents);
        reverse(ds.begin(), ds.end());
        for (auto x : ds)
        {
            for (int i = 0; i < max_len; i++)
            {
                if (i == 0)
                {
                    climb_arr[x][i] = parents[x];
                    continue;
                }
                if (climb_arr[x][i - 1] != -1)
                {

                    climb_arr[x][i] = climb_arr[climb_arr[x][i - 1]][i - 1];
                }
                if (climb_arr[x][i] == -1)
                {
                    break;
                }
            }
        }
    }
    ll add(ll parent)
    {
        climb_arr.push_back(vecl(max_len, -1));
        parents.push_back(parent);
        ll child = parents.size() - 1;
        ll x = child;
        for (int i = 0; i < max_len; i++)
        {
            if (i == 0)
            {
                climb_arr[x][i] = parents[x];
                continue;
            }
            if (climb_arr[x][i - 1] != -1)
            {
                climb_arr[x][i] = climb_arr[climb_arr[x][i - 1]][i - 1];
            }
            if (climb_arr[x][i] == -1)
            {
                break;
            }
        }
        return child;
    }
    ll up(ll x, int k)
    {
        if (k <= 0)
        {
            return x;
        }
        int amount_to_climb = k & (-k);
        int index = log2(amount_to_climb);
        x = climb_arr[x][index];

        if (x == -1)
        {
            return -1;
        }
        ll ans = up(x, k - amount_to_climb);
        return ans;
    }
};
int main()
{
    // freopen("Sample.txt", "r", stdin);
    int n;
    cin >> n;
    mapsl name = mapsl();
    mapls rn = mapls();
    int k = 0;
    n++;
    mapl tree = mapl(n);
    for (int i = 0; i < n - 1; i++)
    {
        string a, b;
        cin >> a >> b;
        if (name.find(a) == name.end())
        {
            name[a] = k;
            rn[k] = a;
            k++;
        }
        if (name.find(b) == name.end())
        {
            name[b] = k;
            rn[k] = b;
            k++;
        }
        tree[name[a]].push_back(name[b]);
        tree[name[b]].push_back(name[a]);
    }
    auto Tc = Tree_Climb(tree, n, name["ROOT"]);
    ll q;
    cin >> q;
    auto delted = set<string>();
    for (int j = 0; j < q; j++)
    {
        string aa, bb, cc;
        ll k;
        cin >> aa;
        if (aa == "N")
        {
            cin >> bb >> cc;
            name[cc] = Tc.add(name[bb]);
            rn[name[cc]] = cc;
        }

        if (aa == "R")
        {
            cin >> bb;
            delted.insert(bb);
        }
        if (aa == "F")
        {
            cin >> bb >> k;
            if (delted.find(bb) != delted.end())
            {
                cout << "None" << endl;
                continue;
            }
            ll v = Tc.up(name[bb], k);

            if (v == -1 || v == name["ROOT"])
            {

                cout << "None" << endl;
                continue;
            }
            cout << rn[v] << endl;
        }
    }

    return 0;
}
