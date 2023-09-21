num = int(input())
string = input()

listString = set(string)
l = list(string)

def checkValid(s):
    odd = s[1::2]
    even = s[::2]
    
    if (len(set(odd)) == 1 and len(set(even)) == 1):
        return True
    else:
        return False

if len(listString) == 1:
    print(0)
    exit()

maximum = 0
for i in listString:
    for j in listString:
        if i == j:
            continue

        newList = [x for x in l if i == x or j == x]
        le = len(newList)
        if checkValid(newList) and maximum < le:
            maximum = le
            

print(maximum)

