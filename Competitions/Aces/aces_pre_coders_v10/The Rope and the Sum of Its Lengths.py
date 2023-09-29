
import os

s = input()

count = len(s)


for i in range(1, len(s)):
    
    new_s = s[:i] + s
    
    ini_strlist = []
    ini_strlist.append(new_s)
    ini_strlist.append(s[i:])
 
    # Using the Python built-in function os.path.commonprefix() to find the common prefix of the list of strings
    prefix = os.path.commonprefix(ini_strlist)
    count+=len(prefix)
    
#     n = 0
#     for j in range(len(s[i:])):
#         if new_s[j] != s[i:][j]:
#             break
#         n+=1
        
#     count += n
    
print(count)


