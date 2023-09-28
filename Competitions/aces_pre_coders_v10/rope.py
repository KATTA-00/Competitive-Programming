s = input()

count = len(s)


for i in range(1, len(s)):
    
    new_s = s[:i] + s
    
    n = 0
    for j in range(len(s[i:])):
        if new_s[j] != s[i:][j]:
            break
        n+=1
        
    count += n
    
print(count)


