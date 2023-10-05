a, b = [int(x) for x in input().strip().split(" ")]

m = -1

for _ in range(a):
    m = max(m, max([int(x) for x in input().strip().split(" ")]))
    
print(m)