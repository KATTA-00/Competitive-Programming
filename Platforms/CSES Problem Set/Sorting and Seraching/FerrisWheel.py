####### two pointers #######

num, weight = map(int,input().strip().split())

wArr = appSizeArr = list(map(int,input().strip().split()))

wArr.sort()
count=num
pointer1=0
pointer2=num-1

while pointer1<pointer2:
    if wArr[pointer1]+wArr[pointer2]<=weight:
        count-=1
        pointer1+=1
        pointer2-=1
    else:
        pointer2-=1

print(count)