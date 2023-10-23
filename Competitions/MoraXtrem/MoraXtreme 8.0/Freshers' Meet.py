def getPower(subSet):
    return sum(subSet)*len(subSet)*2
    
n,m = [int(i) for i in input().strip().split()]

hi = [int(i) for i in input().strip().split()]

for _ in range(m):
    l,r,x = [int(i) for i in input().strip().split()]
    Kmin = 1000000
    found = False
    for i in range(l-1,r):
        for j in range(i+1,r+1):
            # print(hi[i:j])
            # print(getPower(hi[i:j]))
            if getPower(hi[i:j])>=x:
                found = True
                Kmin = min(Kmin,max(hi[i:j]))
    
    if found==True:
        print(Kmin)
    else:
        print(-1)