def seperateNumbers(s):
    len_s = len(s)//2 
    count = 0
    currentValue = 0
    set = 0
    
    for j in range(len_s):
        count+=1
        currentS = str(s[0:count])
        currentValue = int(s[0:count])
        while len(currentS)<len(s):
            currentvalue += 1
            currentS = currentS + str(currentValue)
        if currentS == s:
            print('YES',currentS[:count])
        set = 1
        break
    
    if set==0:
        print('NO')



n = int(input().strip())

for i in range(n):
    s = str(input().strip())
    seperateNumbers(s)



