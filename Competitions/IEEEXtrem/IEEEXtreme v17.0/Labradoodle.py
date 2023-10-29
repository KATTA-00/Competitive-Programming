import os

a, b = map(int, input().strip().split(" "))
dicWords = []
makeWords = []
count = []

for _ in range(a):
    dicWords.append(input().strip())


for _ in range(b):
    word = input().strip()

    l = 0
    temp = []
    # print(word)
    c = 0
    for i in range(3, len(word)):

        left = word[:i]
        if i > len(word)-3:
            i = len(word)-3
            left = word[:i+1]

        right = word[i:]

        # print(left + " " + right)

        for j in dicWords:
            if left in j:
                for r in dicWords:
                    if right in r:
                        if (j, r) not in temp:
                            temp.append((j, r))
                            
                            c+=1
    
    count.append(c)
    makeWords.append(temp)

# print(makeWords)
   
for i in range(b):
    if count[i] == 0:
        print("none")
    elif count[i] > 1:
        print("ambiguous")
    else:
        # print(makeWords[i])
        print(makeWords[i][0][0], makeWords[i][0][1])
    
