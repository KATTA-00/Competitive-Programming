t = int(input())

def getNumber(x, y):
    if x == y:
        if x == 1:
            return 1
        return (x-1)**2 + x
    
    if x > y :
        if x%2 != 0:
            return (x-1)**2 + y
        else:
            return (x-1)**2 + 2* x - y
        
    else:
        if y%2 != 0:
            return (y-1)**2 + 2* y - x
        else:
            return (y-1)**2 + x

# print(getNumber(2,5))

for _ in range(t):
    x, y = map(int, input().strip().split(" "))

    print(getNumber(x, y))