n = int(input())

for i in range (n):
    x, y = map(int,input().split())
    if y > x:
        z = x
        x = y
        y = z

    if (x > 2*y or (x+y)%3 != 0):
        print("NO")
    else:
        print("YES")
