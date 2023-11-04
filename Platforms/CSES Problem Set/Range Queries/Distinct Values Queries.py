n, q = map(int, input().strip().split(' '))

arr = list(map(int, input().strip().split(' ')))

for _ in range(q):
    a, b = map(int, input().strip().split(' '))

    temp = arr[a-1:b]

    # print(temp)

    print(len(set(temp)))