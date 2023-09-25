def gcd(a,b):
    A = max(a,b)
    B = min(a,b)

    if B==0:
        return A
    
    return gcd(B,A%B)

print(gcd(20,15))