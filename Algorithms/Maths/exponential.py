def exponentiation(bas, exp):
    N=10**9+7
    t = 1
    while(exp > 0):
        if (exp % 2 != 0):
            t = (t * bas) % N
 
        bas = (bas * bas) % N
        exp = int(exp / 2)
        
    return t % N

t = int(input())
for i in range(t):
    a,b=[int(j) for j in input().split()]

    print(exponentiation(a,b))