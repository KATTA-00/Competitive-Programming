n, m = map(int, input().strip().split(" "))

rym = []
rymVisited = [False] * n
realVisited = [False] * n

for _ in range(n):
    rym.append(input().strip().split(" "))

def letterMap(n):
    return chr(ord('A') + n)

space = input()

ss = []
rymMap = {}
keyMapping = {}
realKeyMapping = {}

count = 0
for _ in range(m):
    word = input().strip().split(" ")[-1].lower()

    for i in range(n):
        if word in rym[i]:

            if rymVisited[i]:
                realVisited[i] = True

            rymVisited[i] = True

            x = rymMap.get(i, None)
            if x == None:
                rymMap[i] = rym[i]
                keyMapping[i] = count
                count += 1

            ss.append(i)
            break
    else:
        ss.append(-1)


for i in range(n):
    if not realVisited[i]:
        keyMapping[i] = -1

c = 0
for i in keyMapping:
    if keyMapping[i] != -1:
        realKeyMapping[i] = c
        c+=1

c = 0
output = ""
for i in ss:
    if i==-1:
        output+="X"
    else:
        if realVisited[i]:
            output += letterMap(realKeyMapping[i])
        else:
            output+="X"


print(output)