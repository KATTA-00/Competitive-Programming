n, k = map(int, input().strip().split(" "))

def numberToBase(n, b):
    if n == 0:
        return "0"
    
    digits = []
    while n:
        digits.append(str(n % b))
        n //= b
        
    return "".join(digits[::-1])

c = 0
for i in range(1, n):
    s = str(i)
    if s == s[::-1]:
        b = numberToBase(i,k)
        if b == b[::-1]:
            c+=i
            
print(c)