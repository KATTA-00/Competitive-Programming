import os

s = input()

count = len(s)


for i in range(1, len(s)):
    
    new_s = s[:i] + s
    
    ini_strlist = []
    ini_strlist.append(new_s)
    ini_strlist.append(s[i:])
 
    prefix = os.path.commonprefix(ini_strlist)
    count+=len(prefix)
    
print(count)


