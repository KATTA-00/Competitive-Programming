n = int(input().strip())

set1 = []
set2 = []

if (n+1)%4 == 0:
    twoAddSet = 1
    for i in range(0,n+1,4):
        if twoAddSet == 1:
            if i!=0:
                set2.append(i)
            set1.append(i+1)
            set1.append(i+2)
            set2.append(i+3)
            twoAddSet = 2

        else:
            set1.append(i)
            set2.append(i+1)
            set2.append(i+2)
            set1.append(i+3)
            twoAddSet = 1

    print("YES")
    print(len(set1))
    for num in set1:
        print(num, end=" ")
    print(len(set2))
    for num in set2:
        print(num, end=" ")

elif n%4 == 0:
    twoAddSet = 1
    for i in range(1,n+1,4):
        if twoAddSet == 1:
            if i!=0:
                set2.append(i)
            set1.append(i+1)
            set1.append(i+2)
            set2.append(i+3)
            twoAddSet = 2

        else:
            set1.append(i)
            set2.append(i+1)
            set2.append(i+2)
            set1.append(i+3)
            twoAddSet = 1

    print("YES")
    print(len(set1))
    for num in set1:
        print(num, end=" ")
    print(len(set2))
    for num in set2:
        print(num, end=" ")

else:
    print('NO')
    

