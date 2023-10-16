DEBUG = True

if(DEBUG):
    import os
    os.chdir(os.path.dirname(__file__))
    
    global input
    f = open("Sample.txt")
    input = lambda :f.readline().strip()

n = int(input())

parent = {}

for _ in range(n):
    a, b = list(map(str, input().strip().split(" ")))
    
    parent[a] = b
    
t = int(input())


for _ in range(t):
    s = input()
    
    if s[0] == "N":
        x, a, b = list(map(str, s.split(" ")))
        
        parent[b] = a
    
    elif s[0] == "R":
        x, a= list(map(str, s.split(" ")))

        try:
            del parent[a]
        except:
            pass
        
    else:
        x, a, b = list(map(str, s.split(" ")))
        
        num = int(b)
        
        node = parent.get(a, None)
        
        if node == None:
            print("None")
            continue
            
        for i in range(num-1):
            
            node = parent.get(node, None)
            
            if node == None or node == "ROOT":
                print("None")
                break
        else:
            
            print(node)
        
            
        