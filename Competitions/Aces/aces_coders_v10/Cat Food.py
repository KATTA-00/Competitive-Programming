n =int(input())

for i in range(n):
    print(" "*(n+1),end="")
    print(" "*(n-i-1),end ="")
    print("*"*(1+3*i),end="")

    print(' '*2*(n-i-1), end ="")
    print(" "*2*n,end="")
    print(' '*2*(n-i-1), end ="")
    print("*"*(1+3*i))

for i in range(n//2):
    print(" "*(n+1),end="")
    print("*"*(8*n-4))

for i in range((n+1)//2):
    print(" "*(n+1),end="")
    print("*"*n,end="")
    print(" "*n,end="")
    print("*"*4*(n-1), end="")
    print(" "*n,end="")
    print("*"*n)

for i in range(n):
    if(i<n//2):
        if i%2==0:
            print(" "*i,end="")
            print("*"*n,end="")
            print(" ",end="")
            print("*"*(3*n-2),end="")
            print(" "*2*(n-i),end="")
            print("*"*(3*n-2),end="")
            print(" ",end="")
            print("*"*n)

        else:
            print(" "*i,end="")
            print(" "*n,end="")
            print(" ",end="")
            # print(" ",end="")
            print("*"*(3*n-2),end="")
            print(" "*2*(n-i),end="")
            print("*"*(3*n-2))

    else:
        if i%2==0:
            print(" "*i,end="")
            print("*"*n,end="")
            print(" ",end="")
            print("*"*(4*n-3-i),end="")
            print("  ",end="")
            print("*"*(4*n-3-i),end="")
            print(" ",end = "")
            print("*"*n)
        else:
            print(" "*i,end="")
            print(" "*n,end="")
            print(" ",end="")
            print("*"*(4*n-3-i),end="")
            print("  ",end="")
            print("*"*(4*n-3-i))

for i in range(n):
    print(" "*(n+n-i),end="")
    print("*"*(8*n-2-2*(n-i)))