#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef pair<ll, ll> pll;
const int maxN = 2e5 + 1;
const int SIZE = 4 * maxN;

int N, Q, lo[SIZE], hi[SIZE], mp[maxN];
ll sum[SIZE], pre[SIZE];

void pull(int i)
{
    pre[i] = max(pre[2 * i], sum[2 * i] + pre[2 * i + 1]);
    sum[i] = sum[2 * i] + sum[2 * i + 1];
}

void init(int i, int l, int r)
{
    lo[i] = l;
    hi[i] = r;
    if (l == r)
    {
        cin >> sum[i];
        pre[i] = max(0LL, sum[i]);
        mp[l] = i;
        return;
    }
    int m = (l + r) / 2;
    init(2 * i, l, m);
    init(2 * i + 1, m + 1, r);
    pull(i);
}

void update(int idx, int val)
{
    int i = mp[idx];
    sum[i] = val;
    pre[i] = max(0LL, sum[i]);

    i >>= 1;
    while (i)
    {
        pull(i);
        i >>= 1;
    }
}

pll query(int i, int l, int r)
{
    if (l > hi[i] || r < lo[i])
        return {0, 0};
    if (l <= lo[i] && hi[i] <= r)
        return {pre[i], sum[i]};

    pll left = query(2 * i, l, r);
    pll right = query(2 * i + 1, l, r);
    return {max(left.first, left.second + right.first), left.second + right.second};
}

int main()
{
    cin >> N >> Q;
    init(1, 1, N);
    for (int q = 0, t, a, b; q < Q; q++)
    {
        cin >> t >> a >> b;
        if (t == 1)
            update(a, b);
        else if (t == 2)
            cout << query(1, a, b).first << endl;
    }
}

// 1. **Header Includes:**
//    ```cpp
//    #include <bits/stdc++.h>
//    ```
//    This line includes the standard C++ libraries, which contain commonly used functions and data structures.

// 2. **Type Definitions:**
//    ```cpp
//    using namespace std;
//    typedef long long ll;
//    typedef pair<ll, ll> pll;
//    ```
//    These lines define some type aliases:
//    - `ll` is an alias for `long long` data type.
//    - `pll` is an alias for a pair of `long long` values.

// 3. **Constants and Variables:**
//    ```cpp
//    const int maxN = 2e5+1;
//    const int SIZE = 4*maxN;
//    int N, Q, lo[SIZE], hi[SIZE], mp[maxN];
//    ll sum[SIZE], pre[SIZE];
//    ```
//    - `maxN` and `SIZE` are constants used to define the maximum size of the array and the size of the segment tree used in this code.
//    - `N` represents the size of the array.
//    - `Q` represents the number of queries.
//    - `lo`, `hi`, and `mp` are arrays used to store information about the segments in the segment tree.
//    - `sum` stores the sum of elements in each segment of the tree.
//    - `pre` stores the maximum prefix sum in each segment of the tree.

// 4. **`pull` Function:**
//    ```cpp
//    void pull(int i){
//        pre[i] = max(pre[2*i], sum[2*i]+pre[2*i+1]);
//        sum[i] = sum[2*i] + sum[2*i+1];
//    }
//    ```
//    This function is used to update the `pre` and `sum` values of a node in the segment tree based on its children. It calculates the maximum prefix sum and the sum of elements for the given node.

// 5. **`init` Function:**
//    ```cpp
//    void init(int i, int l, int r){
//        // ...
//    }
//    ```
//    This function initializes the segment tree. It takes as arguments the current node `i`, the left index `l`, and the right index `r` of the segment.

//    - If `l` is equal to `r`, it means that the function has reached a leaf node (individual element of the array), and it reads the value from the input, initializes `sum` and `pre` for that node, and stores the mapping from the array index to the segment tree node in the `mp` array.

//    - If `l` is not equal to `r`, it recursively calls `init` for its left and right children and then uses the `pull` function to update the values for the current node based on its children.

// 6. **`update` Function:**
//    ```cpp
//    void update(int idx, int val){
//        // ...
//    }
//    ```
//    This function updates the value of an element in the array at position `idx` with the new value `val`. It then updates the corresponding node in the segment tree and propagates the changes upwards in the tree using the `pull` function.

// 7. **`query` Function:**
//    ```cpp
//    pll query(int i, int l, int r){
//        // ...
//    }
//    ```
//    This function is used to answer queries for finding the maximum prefix sum in a given range `[l, r]`. It recursively traverses the segment tree to find the maximum prefix sum in the specified range.

// 8. **`main` Function:**
//    ```cpp
//    int main(){
//        // ...
//    }
//    ```
//    The `main` function is the entry point of the program.

//    - It first reads the values of `N` and `Q` from the input.

//    - It initializes the segment tree using the `init` function.

//    - It then processes a series of queries in a loop. Each query is of one of two types:
//      - Type 1: Update the value of an element in the array.
//      - Type 2: Query for the maximum prefix sum in a specified range.
