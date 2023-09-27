n = int(input())
l = list(map(int, input().split()))

sort = sorted(l)
rev = list(reversed(l))
swaps = 0
swaps_rev = 0

dic1 = {}
for i in range(n):
    if sort[i] not in dic1:
        dic1[sort[i]] = i

i = 0
while i < n:
    if sort[i] == l[i]:
        i += 1
        continue
    swaps += 1
    l[dic1[l[i]]], l[i] = l[i], l[dic1[l[i]]]


dic2 = {}
for i in range(n):
    if sort[i] not in dic2:
        dic2[sort[i]] = i

i = 0
while i < n:
    if sort[i] == rev[i]:
        i += 1
        continue
    swaps_rev += 1
    rev[dic2[rev[i]]], rev[i] = rev[i], rev[dic2[rev[i]]]

print(min(swaps, swaps_rev))