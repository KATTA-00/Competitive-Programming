size, queries = [int(x) for x in input().strip().split(" ")]
arr = [int(x) for x in input().strip().split(" ")]

maximum = 2*10**5+1

ds = [0 for x in range(maximum)]

def update(x, val):
     
    while x<=size:
        ds[x] += val
        x += -x&x

def query(x):
    sum = 0

    while x>0:
        sum += ds[x]
        x -= -x&x

    return sum


for i in range(1, len(arr)+1):
    update(i, arr[i-1])
    update(i+1, -arr[i-1])


for i in range(queries):
    q = [int(x) for x in input().strip().split(" ")]

    if q[0] == 1:
        update(q[2]+1, -q[3])
        update(q[1], q[3])
    else:
        print(query(q[1]))

