m = 10**9

def product(A, B):
    num1 = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    num2 = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    num3 = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    num4 = A[1][0] * B[0][1] + A[1][1] * B[1][1]
    num1 %= m
    num2 %= m
    num3 %= m
    num4 %= m
    return ((num1, num3), (num2, num4))

def expo(A, v):
    if v == -1:
        return 0
    if v == 0:
        return ((1, 0), (0, 1))
    if v == 1:
        return A
    
    B = expo(A, v // 2)
    if v % 2:
        return product(product(B, B), A)
    else:
        return product(B, B)

T = int(input())
for _ in range(T):
    N = int(input())
    A = (1, 0)
    B = ((1, 1), (1, 0))
    B = expo(B, N-1)
    print(B[0][0])