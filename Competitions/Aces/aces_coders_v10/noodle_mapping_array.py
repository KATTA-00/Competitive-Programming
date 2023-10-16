n = int(input())

parent = [-1] * (10**5 + 1)
mapping = {}
rev_mapping = {}

count = 0

def get_or_create_mapping(name):
    global count
    if name not in mapping:
        mapping[name] = count
        rev_mapping[count] = name
        count += 1
    return mapping[name]

for _ in range(n):
    a, b = input().strip().split()

    parent[get_or_create_mapping(a)] = get_or_create_mapping(b)

t = int(input())

for _ in range(t):
    s = input()

    if s[0] == "N":
        _, a, b = s.split()
        parent[get_or_create_mapping(b)] = mapping[a]
    
    elif s[0] == "R":
        _, a = s.split()
        parent[get_or_create_mapping(a)] = -1
    
    else:
        _, a, b = s.split()
        num = int(b)
        
        node = get_or_create_mapping(a)
        
        for i in range(num):
            if node == -1:
                break  
                
            node = parent[node]
            
        if node == -1 or node == 0:
            print("None")
        else:
            print(rev_mapping[node])
