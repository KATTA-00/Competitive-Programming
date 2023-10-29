def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

def canFill(a,b,c):
    if c % gcd(a, b) == 0 and c <= max(a, b):
        print("YES")
        return

    print("NO")
    return

n = int(input().strip())

for i in range(n):
    a,b,c = tuple(map(int,input().split()))
    canFill(a,b,c)
    
    


