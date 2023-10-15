n = int(input())

class Node:
    def __init__(self, name, net):
        self.name = name
        self.net = net
        
node = []

def find(s):
    for i in node:
        if i.name == s:
            return i
    return None

def deleteNode(s):
    for i in range(len(node)):
        if node[i].name == s:
            del node[i]
            return 0
    
for _ in range(n):
    t1, t2 = list(map(str, input().strip().split()))
    
    if t2 == "ROOT":
        n0 = Node(t2, None)
        node.append(n0)
        n = Node(t1, n0)
        node.append(n)
    else:
        n = Node(t1, find(t2))
        node.append(n)

num = int(input())

for _ in range(num):
    # l = [n.name for n in node]
    # print(l)
    
    ss = input()

    if ss[0] == "N":
        temp, t1, t2 = list(map(str, ss.split(" ")))
        n = Node(t2, find(t1))
        node.append(n)
        
    elif ss[0] == "R":
        temp, t1 = list(map(str, ss.split(" ")))
        deleteNode(t1)
        
    else:
        temp, t1, t2 = list(map(str, ss.split(" ")))
        t2 = int(t2)
        n = find(t1)
        
        if n == None:
            print("None")
            continue
        
        flag = False
        for i in range(t2):
            if n.net == None:
                print("None")
                flag = True
                break
            n = n.net
            
        if flag:
                continue
            
        print(n.name)


