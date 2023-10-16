# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def combinations(n, r): 
    if n < r:
        return 0

    result = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
    return result


T = int(input())

for _ in range(T):
    K, S, a, b = list(map(int, input().split()))
    
    new = K - S
    
    
    total_ways = combinations(new,a)*combinations(new-a,b)
    print(total_ways)
