n,m =[int(i) for i in input().strip().split()]

x = int(input())

n = n-2*(x-1)
m = m-2*(x-1)

if(n<0 or m<0):
    print(0)
    
if n==1:
    if m%2==0:
        print(m//2)
    else:
        print(m//2+1)
        
elif m==1:
    if n%2==0:
        print(n//2)
    else:
        print(n//2+1)
    
else:
    print(n+m-2)