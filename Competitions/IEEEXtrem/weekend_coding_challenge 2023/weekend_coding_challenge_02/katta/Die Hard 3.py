num = int(input())

for i in range(num):
    a, b, c = [int(x) for x in input().strip().split(" ")]
    
    if c > a and c > b:
        print("NO")
        continue

    print("YES")