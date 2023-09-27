#Sieve of Eratosthenes
# def SOE(n):
#     primes = []
#     val = [True for i in range(n+1)]
#     val[0] = val[1] = False
#     for ind in range(2,int(n**0.5)+1):
#         if val[ind]:
#             for x in range(ind**2,n+1,ind):
#                 val[x]=False
#     for y in range(n+1):
#         if val[y]:
#             primes.append(y)
#     return primes

# print(SOE(2*10**6))


##########################################

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1 
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes


n = 2*10**6
primes = sieve_of_eratosthenes(n)
print(primes)