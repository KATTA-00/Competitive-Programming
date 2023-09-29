def getTime(s):
    s = s.split(':')

    return int(s[0]) + float("0." + s[1])


num = int(input())

shedule = []
for i in range(num):
    data = input().split(" ")
    if (data[0] == "Y"):
        shedule.append([getTime(data[1]), getTime(data[2])])


g = []
shedule = sorted(shedule, key=lambda x: x[0])
for i in range(len(shedule)-1):
    start = shedule[i]
    temp = []
    for j in range(i+1, len(shedule)):
        
        if (start[1] <= shedule[j][0]):
            temp.append(j)
    
    # g.append(count)
    g.append(temp)
    
f = [0 for x in range(len(shedule))]
visit = [0 for x in range(len(shedule))]
def dfs(i, count):
    visit[i] = 1
    if f[i] < count:
        f[i] = count
        
    if visit == 1:
        return 0
    
    if i == len(shedule)-1:
        return 0
    
    count += 1
    for j in g[i]:
        dfs(j, count)
        
for i in range(len(g)):
    dfs(i, 1)

# print(g)
# print(f)
if len(g) == 0:
    print(1)
else:
    print(max(f))
