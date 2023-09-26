t = int(input())

def prime(n):
    
    if (n == 1):
        return False

    for i in range(2, n + 1):
        if i * i > n:
            break
        if (n % i == 0):
            return False

    return True


def minDivisor(n):

    if (prime(n)):
        print(1, n - 1)

    else:
        for i in range(2, n + 1):
            if i * i > n:
                break

            if (n % i == 0):

                print(n // i, n // i * (i - 1))
                break

for _ in range(t):
    n = int(input())
    minDivisor(n)
    