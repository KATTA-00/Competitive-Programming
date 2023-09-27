def pairs(k, arr):
    arr_set = set(arr)
    count = 0
    
    for num in arr:       
        if num + k in arr_set:
            count += 1
    
    return count


n, k = map(int, input().split())
arr = list(map(int, input().split()))

result = pairs(k, arr)
print(result)
