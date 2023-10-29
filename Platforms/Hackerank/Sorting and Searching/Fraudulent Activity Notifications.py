num, days = [int(x) for x in input().strip().split(' ')]
spending = [int(x) for x in input().strip().split(' ')]

even = False
if days%2 == 0:
    even = True
mid = days/2

def getMedian(arr):
    arr.sort()
    print(arr)
    l = len(arr)

    if (l == 1):
        return arr[0]

    if even:
        return (arr[mid]+arr[mid+1])/2
    else:
        return arr[int(mid)]

count = 0
for i in range(days,num):
    print(spending[i-days:i])
    print(getMedian(spending[i-days:i]), spending[i] )

    if (getMedian(spending[i-days:i])*2 <= spending[i]):
        count += 1

print(count)