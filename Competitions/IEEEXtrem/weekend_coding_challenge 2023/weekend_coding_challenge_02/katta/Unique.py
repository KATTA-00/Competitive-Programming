test = int(input())

for i in  range(test):
    num = int(input())
    s = input()
    
    ss = set(s)
    
    temp = len(s) - len(ss)
    
    if (temp + len(s) > 26):
        print(-1)
        continue

        
    print(temp)
        
         
        