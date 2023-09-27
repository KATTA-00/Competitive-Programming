def shortPalindrome(s):

    dim1 = {} # dim1[c] - number of times character c has been seen so far
    dim2 = {} # dim2[(c, i)] - number of tuples of (c, i) characters seen so far
    dim3 = {} # dim3[i] - number of tuples of (c, c, i) tuples seen so far
    count = 0
    mod = 7 + 10**9

    for k in s:
        c = ord(k) - ord('a')
        count = (count + dim3.get(c, 0)) % mod
        ic = c

        for i in range(26):
            dim3[i] = (dim3.get(i, 0) + dim2.get((ic, i), 0)) % mod
            dim2[(ic, i)] = (dim2.get((ic, i), 0) + dim1.get(i, 0)) % mod
            ic += 26

        dim1[c] = dim1.get(c, 0) + 1
    return count

s = input()
print(shortPalindrome(s))
