class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


dsu = DSU(10**5)
inLinst = [False] * 10**5
hora = []
def find_sources(rumors):
    global nameMapping, parent, revNameMapping
    count = 0

    for rumor in rumors:
        if "??" in rumor:
            p1, p2 = rumor.split(" ?? ")

            if p1 not in nameMapping:
                nameMapping[p1] = count
                revNameMapping[count] = p1
                count+=1

            if p2 not in nameMapping:
                nameMapping[p2] = count
                revNameMapping[count] = p2
                count+=1

            if p1 in hora or p2 in hora:
                inLinst[nameMapping[p1]] = True
                inLinst[nameMapping[p2]] = True

            dsu.union(nameMapping[p1], nameMapping[p2])

        elif "->" in rumor:
            p1, p2 = rumor.split(" -> ")
            hora.append(p1)

            if p1 not in nameMapping:
                nameMapping[p1] = count
                revNameMapping[count] = p1
                count+=1

            if p2 not in nameMapping:
                nameMapping[p2] = count
                revNameMapping[count] = p2
                count+=1

            dsu.union(nameMapping[p1], nameMapping[p2])
            parent[nameMapping[p2]] = nameMapping[p2]
            inLinst[nameMapping[p1]] = True
            inLinst[nameMapping[p2]] = True
            

n = int(input())
rumors = [input() for _ in range(n)]
nameMapping = {}
revNameMapping = {}
parent = [-1] * 10 ** 5

ru = []
for i in rumors:
    if "->" in i:
        ru.append(i)

for i in rumors:
    if "??" in i:
        ru.append(i)

find_sources(ru)
num = len(nameMapping)
parent = parent[:num]

common = set()

for i in parent:
    if i != -1:
        for j in parent:
            if dsu.find(i) == dsu.find(j):
                common.add(revNameMapping[i])

temp = []
for i in nameMapping:
    if i not in common and inLinst[nameMapping[i]]:
        temp.append(i)
        
temp.reverse()
for i in temp:
    print(i)

