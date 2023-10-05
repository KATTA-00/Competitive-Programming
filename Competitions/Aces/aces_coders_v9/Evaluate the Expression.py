
def getCal(op):
    # print(">> ", op)
    if op == "*":
        c = 1
    else:
        c = 0
        
    flag = True
    
    p = input().strip()
    while p != "{/" + op + "}":
        # print(p)
        if p[0] != "{":
            if op == "+":
                c += int(p)
            elif op == "*":
                c *= int(p)
            elif op == "-":
                if flag:
                    c += int(p)
                    flag = False
                else:
                    c -= int(p)
        else:
            if op == "+":
                c += getCal(p[1])
            elif op == "*":
                c *= getCal(p[1])
            elif op == "-":
                if flag:
                    c += getCal(p[1])
                    flag = False
                else:
                    c -= getCal(p[1])
            
        p = input().strip()
    
    # print(">>>>>> ", c)
    return c
    
    
s = input().strip()
if s == "#":
    print(0)
else:
    print(getCal(s[1]))
        
    
