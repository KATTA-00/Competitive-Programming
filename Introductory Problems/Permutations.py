
num = int(input())

if num == 1:
    print(1)
elif num < 4 :
    print("NO SOLUTION")
elif num == 4:
    print("2 4 1 3")
else:
    for i in range(1, num+1, 2):
        print(i, end=" ")
    for i in range(2, num+1, 2):
        print(i, end=" ")
    print()