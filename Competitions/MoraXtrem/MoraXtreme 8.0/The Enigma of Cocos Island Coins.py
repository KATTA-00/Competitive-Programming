def sieve_of_eratosthenes(n,psi):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1 
    primes = [i for i in range(psi, n + 1) if is_prime[i]]
    return primes

n,psi = [int(i) for i in input().strip().split()]

if n==1:
    print(psi)

else:
    primes = sieve_of_eratosthenes(10000000,psi)
    if n>len(primes):
        print(0)
    else:
        if primes[n-2]*psi >= 10**9:
            print(0)
        else:
            print(primes[n-2]*psi)
    