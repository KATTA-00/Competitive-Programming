
# power of 2
def isPowerOf2(n):
    if n <= 0:
        return False
    x = n
    y = not (n & (n-1))
    return x and y

# return's number of 1's in binary representation of int
# 5 -> 101 ans = 2
# 7 -> 111 ans = 3


def bruteforcecntbits(n):
    # T.C = O(n)
    s = str(bin(n))[2:]
    print("{}".format(s))
    return s.count('1')


def cntbits(n):
    # T.C = O(logn)
    cnt = 0
    while n:
        cnt += 1
        n = n & (n-1)
    return cnt
