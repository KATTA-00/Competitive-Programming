A = [int(i) for i in input().split()]

N = len(A)

for i in range(2**N):
    for j in range(N):
        if(i & (1<<j)):
            print(A[j], end='')

