def getValues(num, prime):
    arr = []
    while num > 0:
        arr.append(num % prime) 
        num //= prime  
    digits = len(arr) 

    DP1 = [[0] * digits for _ in range(digits + 1)]
    DP2 = [[0] * digits for _ in range(digits + 1)]

    DP1[digits][0] = 1

    for i in range(digits, 0, -1):
        for j in range(digits):
            
            DP1[i - 1][j] = (arr[i - 1] + 1) * DP1[i][j] + (prime - arr[i - 1] - 1) * (DP2[i][j - 1] if j > 0 else 0)
            DP2[i - 1][j] = arr[i - 1] * DP1[i][j] + (prime - arr[i - 1]) * (DP2[i][j - 1] if j > 0 else 0)
    
    while DP1[0][-1] == 0:
        DP1[0].pop()
    
    return DP1[0]
    

t = int(input())
for _ in range(t):
    num, prime = map(int, input().split())
    vals = getValues(num, prime)
    for i in range (len(vals)):
        print(vals[i],end=" ")
    print()