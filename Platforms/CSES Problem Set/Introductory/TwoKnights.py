def noattck(n):
    counts=[0,6]
    if n==1:
        return [0]
    if n==2:
        return counts

    size=3
    while size<=n:
        ways=size**2*(size**2-1)//2 -4*(size-2)*(size-1) # nC2 - ()
        counts.append(ways)
        size+=1

    return counts


n=int(input().strip())

sol=noattck(n)

for num in sol:
    print(num)