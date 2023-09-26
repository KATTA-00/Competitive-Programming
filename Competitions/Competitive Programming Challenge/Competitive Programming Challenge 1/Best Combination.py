test = int(input())

for _ in range(test):
    n, p = map(int, input().strip().split())
    arr = [int(x) for x in input().strip().split()]
    
    arr.sort()  # Sort the player levels initially
    prefix_sum = [0] * n
    
    # Calculate the prefix sum of the sorted array
    prefix_sum[0] = arr[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]
    
    minimum = float('inf')
    # Calculate the minimum stars needed using a sliding window
    for i in range(p-1, n):
        if i-p < 0:
            current_cost = arr[i] * p - (prefix_sum[i])
        else:
            current_cost = arr[i] * p - (prefix_sum[i] - prefix_sum[i - p ])
        minimum = min(minimum, current_cost)
    
    print(minimum)
