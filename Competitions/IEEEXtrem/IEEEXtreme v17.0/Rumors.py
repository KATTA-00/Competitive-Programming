n = int(input())
rumors = [input() for _ in range(n)]

not_sure = {}
imposible = set()
total = set()

for i in rumors:

    if "??" in i:
        a, b = i.split(" ?? ")
        not_sure[a] = b
        not_sure[b] = a
        total.add(a)
        total.add(b)
    else:
        a, b = i.split(" -> ")
        imposible.add(b)
        total.add(a)
        total.add(b)

p = set()

for i in imposible:
    if i in not_sure:
        p.add(not_sure[i])
        
    p.add(i)


for i in p:
    if i in not_sure:
        imposible.add(not_sure[i])
        
    imposible.add(i)

# print(p)
# print(imposible)

q = total-imposible
q = list(q)
q.sort()

for i in q:
    print(i)
