def seperateNumbers(s):
    len_s = len(s)//2 
    currentValue = 0
    set = 0
    
    for j in range(1,len_s+1):
        currentValue = int(s[0:j])
        currentS = str(s[0:j])
        while len(currentS)<len(s):
            currentValue += 1
            currentS = currentS + str(currentValue)
        if currentS == s:
            print('YES',currentS[:j])
            return
    
    
    print('NO')



n = int(input().strip())

for i in range(n):
    s = input().strip()
    seperateNumbers(s)



