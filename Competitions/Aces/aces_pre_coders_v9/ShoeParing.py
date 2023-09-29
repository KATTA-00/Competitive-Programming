n = int(input())
arr = list(map(int,input().strip().split()))
count = 0
elements = dict.fromkeys(arr,0)

for items in arr:
    elements[items] += 1

for items in elements:
    if (elements[items]) > 1:
        count += (elements[items])//2
print(count)