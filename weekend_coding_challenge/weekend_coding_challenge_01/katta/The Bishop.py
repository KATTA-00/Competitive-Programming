i = input().split(" ")
a = int(i[0])
b = int(i[1])
c = int(i[2])
d = int(i[3])

p = b - a
q = a + b

if (d == c + p or d == -c + q):
    print(1)
elif (((a+b) % 2) == ((c + d) % 2) ):
    print(2)
else:
    print(-1)