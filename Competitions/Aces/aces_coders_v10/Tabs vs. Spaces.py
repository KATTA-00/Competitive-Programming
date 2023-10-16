n = int(input())

for _ in range(n):
    a, b = list(map(str, input().strip().split(" ")))
    
    if a == b:
        print("True")
        continue
        
    l_a = len(a)
        
    if l_a < len(b):
        print("False")
        continue
    
    c = 0
    l = 0
    flag = False
    while c < l_a:
        
        if l >= len(b):
            print("False")
            flag = True
            break
        
        if a[c] != b[l]:
            
            if a[c] == "T":
                print("False")
                flag = True
                break
                
            if a[c] == "S" and l_a > c+1 and a[c+1] == "S" and b[l] == "T":
                c+=2
                l+=1
            else:
                print("False")
                flag = True
                break
        else:
            c+=1
            l+=1
            
    if not flag:
        print("True")
            
            
            
            
    
    