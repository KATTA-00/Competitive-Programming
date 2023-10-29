n, m = list(map(int , input().strip().split(" ")))

s = input()

for _ in range(m):
    a, b = list(map(int , input().strip().split(" ")))
    a-=1

    ss = s[a:b]
    l = list(s)
    del l[a:b]
    
    s = "".join(l)
    s += ss

print(s)