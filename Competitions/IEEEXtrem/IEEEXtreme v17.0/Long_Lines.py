n, h0, a, c, q = [int(i) for i in input().strip().split()]
countNoticable = 0
Noticable =[]
Noticable.append(h0)

for i in range(1, n):
    h = (a * h0 + c) % q
    
    countNoticable+=len(Noticable)
    
    temp = Noticable.copy()
    for element in temp:
        if h>=element:
            Noticable.remove(element)
    
    h0 = h
    Noticable.append(h)

print(countNoticable)
