import os

s1 = input()
s2 = input()
 
ini_strlist = []
ini_strlist.append(s1)
ini_strlist.append(s2)

prefix = os.path.commonprefix(ini_strlist)
    
print(prefix)


