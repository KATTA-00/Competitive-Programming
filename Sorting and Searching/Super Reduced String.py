string = input()

l = list(string)

myList = l.copy()

flag = True

while(flag):
    flag = False

    for i in range(len(l)-1):
        if(l[i] == l[i+1]):
            l[i] = "$"
            l[i+1] = "$"
            flag = True

    l = [x for x in l if x != "$"]


if(len(l) == 0):
    print("Empty String")
else:
    print("".join(l))