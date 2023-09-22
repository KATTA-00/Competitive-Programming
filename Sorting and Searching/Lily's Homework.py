num = int(input())

homework = [int(x) for x in input().strip().split(" ")]
tempHome = homework.copy()
tempCopy = homework.copy()


homework.sort()
count1 = 0
for i in range(num-1):
    
    if homework[i] == tempHome[i]:
        continue
    
    for j in range(i+1, num):
        
        if homework[i] == tempHome[j]:
            temp = tempHome[j]
            tempHome[j] = tempHome[i]
            tempHome[i] = temp
            count1 += 1
            break

            
homework.reverse()
print(homework)
print(tempCopy)
count2 = 0
for i in range(num-1):
    
    if homework[i] == tempCopy[i]:
        continue
    
    for j in range(i+1, num):
        
        if homework[i] == tempCopy[j]:
            temp = tempCopy[j]
            tempCopy[j] = tempCopy[i]
            tempCopy[i] = temp
            count2 += 1
            break
        
    print(tempCopy)

if count1 < count2:
    print(count1)
else:
    print(count2)
