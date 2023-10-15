num = int(input())

mapping = {}
MAXN = 10**5 + 1
MAXD = 30

parent = [[0] * MAXD for x in range(MAXN)]

def jump(a, b):

    for i in range(MAXD):
        
        if (b  & (1<<i)):
            
            a = parent[a][i]

    return a

count = 1
for _ in range(num):
    t1, t2 = list(map(str, input().strip().split()))

    if t2 not in mapping:
        mapping[t2] = count
        count+=1

    if t1 not in mapping:
        mapping[t1] = count
        count+=1

    parent[mapping[t1]][0] = mapping[t2] 

for d in range(1, MAXD):
    for i in range(1, num+1):
        parent[i][d] = parent[parent[i][d-1]][d-1]


num = int(input())

for _ in range(num):
    ss = input()

    if ss[0] == "N":
        temp, t1, t2 = list(map(str, ss.split(" ")))
        if t2 not in mapping:
            mapping[t2] = count
            count+=1

        if t1 not in mapping:
            mapping[t1] = count
            count+=1

        parent[mapping[t1]][0] = mapping[t2] 

        for d in range(1, MAXD):
            for i in range(1, num+1):
                parent[i][d] = parent[parent[i][d-1]][d-1]
        
    elif ss[0] == "R":
        temp, t1 = list(map(str, ss.split(" ")))
        
        
        
    else:
        temp, t1, t2 = list(map(str, ss.split(" ")))
        t2 = int(t2)
        n = find(t1)
        
        if n == None:
            print("None")
            continue
        
        flag = False
        for i in range(t2):
            if n.net == None:
                print("None")
                flag = True
                break
            n = n.net
            
        if flag:
                continue
            
        print(n.name)
