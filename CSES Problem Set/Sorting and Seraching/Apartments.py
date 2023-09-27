numApplicant, numAppartment, dif = map(int,input().strip().split())

desSizeArr = list(map(int,input().strip().split()))
appSizeArr = list(map(int,input().strip().split()))

desSizeArr.sort()
appSizeArr.sort()

i = 0 # - application count
j = 0 # - appartment count
count = 0
 

while i<numApplicant and j<numAppartment:
    if desSizeArr[i] > appSizeArr[j]+dif:
        j += 1
    elif desSizeArr[i] + dif < appSizeArr[j]:
        i += 1
    else:
        j += 1
        i += 1
        count += 1

print(count)

#### Two pointer technique ####
'''
- If the applicant's desired size is greater than the current apartment's size plus dif, move to the next apartment (j++).

- If the applicant's desired size plus dif is less than the current apartment's size, move to the next applicant (i++).

- If neither condition is met, a valid pair is found; increment both i and j and increase the match count (count).
'''
