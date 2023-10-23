import sys

t  = int(input())

if t==1 or t==0:
    print("0.00")
else:
    allBoxes = []

    for _ in range(t):
        allBoxes.append(set(input().strip()))

    m = max(max(box) for box in allBoxes)

    possibleCount=0
    for i in range(t):
        for j in range(i+1,t):
            temp = allBoxes[i].union(allBoxes[j])
            # print(temp)
            # print(len(temp))
            if len(temp)==int(m)+1:
                possibleCount+=1

    allPoss = t*(t-1)//2

    prob = round(possibleCount/allPoss,2)
    print("{:.2f}".format(prob))
        