t = int(input())

for _ in range(t):
    p,q = [int(i) for i in input().strip().split()]
    
    n = int(input())
    
    powers = [int(i) for i in input().strip().split()]
    
    totalpow = sum(powers)
    minimumTimes = totalpow//(p+q) if totalpow%(p+q)==0 else totalpow//(p+q)+1
    print(minimumTimes)