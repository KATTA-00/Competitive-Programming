
def solve(a,b,c):
    # print(">> ")
    v6 = 1
    v9 = a+b

    for i in range(1,c+1):       
        j = (2*a*i-b)//(2*b)+1
        v13 = abs(a*i-j*b)

        if v9* i > v13*v6:
            v6 = i
            v9 = v13
    
    print(v6)  

t = int(input())

for i in range(t):
    a,b,c = [int(i) for i in input().strip().split()]
    solve(a,b,c)  