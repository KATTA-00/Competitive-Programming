from math import *

# gives a array of true and false
def genprimes(n):
    primes = [True]*(n+1)
    primes[0] = False
    primes[1] = False
    for p in range(2, int(sqrt(n))+1):
        if primes[p] == True:
            for i in range(p*p, n+1, p):
                primes[i] = False

    return primes


def isPrime(n):
    if n == 0 or n == 1:  
        return False
    if n == 2 or n == 3: 
        return True
    if n % 2 == 0 or n % 3 == 0: 
        return False
    for i in range(5, int(sqrt(n))+1): 
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True


t = int(input())
while t:
    n = int(input())
    print(*genprimes(n))
    t = t-1
