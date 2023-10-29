n, t = list(map(int, input().strip().split(" ")))

arr = input().replace(" ", "")

for _ in range(t):
    arr = arr.replace("01", "10")
    
print(arr)
            