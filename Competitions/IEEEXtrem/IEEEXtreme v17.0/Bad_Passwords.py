n = int(input())
import os
groups = []

for _ in range(n):
    s = input().strip().split(" ")[1:]
    groups.append(s)

m = int(input())

# print(groups)
for _ in range(m):

    a, b = input().strip().split(" ")

    ini_strlist = []
    ini_strlist.append(a)
    ini_strlist.append(b)
    start = len(os.path.commonprefix(ini_strlist))

    ini_strlist = []
    ini_strlist.append(a[::-1])
    ini_strlist.append(b[::-1])
    end = len(os.path.commonprefix(ini_strlist))

    if start == 0 and end == 0:
        print("OK")
        continue
    else:
        print("REJECT")


    # print(a[start:len(a) - end])