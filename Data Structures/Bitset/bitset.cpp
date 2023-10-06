// C++ program for the above approach

#include <bits/stdc++.h>
using namespace std;
#define Max 100005

// Function to find all distinct
// absolute difference of all
// possible pairs of the array
void printUniqDif(int n, int a[])
{

    // bset[i]: Check if i is present
    // in the array or not
    bitset<Max> bset;

    // diff[i]: Check if there exists a
    // pair whose absolute difference is i
    bitset<Max> diff;

    // Traverse the array, arr[]
    for (int i = 0; i < n; i++)
    {

        // Add in bitset
        bset.set(a[i]);
    }

    // Iterate over the range[0, Max]
    for (int i = 0; i <= Max; i++)
    {

        // If i-th bit is set
        if (bset[i])
        {

            // Insert the absolute difference
            // of all possible pairs whose
            // first element is arr[i]
            diff = diff | (bset >> i);
        }
    }

    // Printing the distinct absolute
    // differences of all possible pairs
    for (int i = 1; i <= Max; i++)
    {

        // If i-th bit is set
        if (diff[i])
        {
            cout << i << " ";
        }
    }
}

// Driver Code
int main()
{

    // Given array
    int a[] = {1, 4, 6};

    // Given size
    int n = sizeof(a) / sizeof(a[0]);

    // Function Call
    printUniqDif(n, a);

    return 0;
}

// Bitset represents a fixed-size sequence of N bits and stores values either 0 or 1.
// Zero means value is false or bit is unset and one means value is true or bit is set.
// Bitset class emulates space efficient array of boolean values, where each element occupies only one bit.

// As it emulates array, its index also starts from 0th position.
// Individual bit from bitset can be accessed using subscript operator. For instance to access first element of bitset foo use foo[0].
