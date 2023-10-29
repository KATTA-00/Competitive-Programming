s = input()

l = 0
ll = len(s)
# print(ll)
m = 1
while(l<ll-1):

    flag = False
    if s[l] == s[l+1]:
        start = s[l]
        count = 0
        while l<ll and start == s[l]:
            # print(s[l], l)
            l+=1
            flag = True
            count += 1

        if count > m:
            m = count

    if flag == False:
        l+=1

print(m)