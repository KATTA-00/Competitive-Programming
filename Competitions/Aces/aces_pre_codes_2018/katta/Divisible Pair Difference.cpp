#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> vl;
typedef vector<int> vi;

int main()
{
    ios_base::sync_with_stdio(false);

    ll n, qq;
    cin >> n >> qq;

    vl a(n);

    for (ll i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    for (ll i = 0; i < qq; i++)
    {
        ll q;
        cin >> q;
        vi r(q, 0);
        for (ll j = 0; j < n; j++)
        {
            r[a[j] % q]++;
        }
        ll sm = 0;
        for (ll j = 0; j < n; j++)
        {
            sm += r[a[j] % q] - 1;
        }
        cout << sm / 2 << endl;
    }

    return 0;
}

// Modulus and Differences:
// The code uses the modulus operator % to find the remainder when dividing an array element by a query integer q.
// If two numbers have a difference that is divisible by q, it means they must have the same remainder when divided by q. In other words, they have the same modulus with respect to q.

// Tracking Modulus Counts:
// For each element in the array, the code counts how many elements have the same remainder when divided by q (the modulus). This count is stored in an array r, where r[i] represents the count of elements with a remainder of i when divided by q.

// Finding Pairs with Differences Divisible by q:
// For each element a[j] in the array, the code increments the count in the r array for the remainder of a[j] when divided by q. This effectively keeps track of how many other elements in the array have the same modulus as a[j].

// Calculating the Total Pairs:
// After processing all elements in the array, the code iterates through the array again. For each element a[j], it calculates the sum sm by subtracting 1 from the count in r for the remainder of a[j] when divided by q. This subtraction of 1 is done to avoid counting the element a[j] itself.
// The reason for this subtraction is that when you find an element a[j] that has the same modulus as another element a[k] with k != j, you effectively found a pair. However, you've counted this pair twice, once for a[j] and once for a[k]. To avoid double-counting, you subtract 1 from the count.

// Dividing by 2 to Correct for Double Counting:
// Since you've counted each pair twice (once for each element in the pair), you divide the sm (the sum of counts) by 2. This step ensures that you're only counting each pair once in the final answer.