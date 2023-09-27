def countSort(arr):
    max_value = max(arr, key=lambda x: int(x[0]))  # Find the maximum value in the array
    max_index = int(max_value[0])

    for i in range(len(arr) // 2):
        arr[i][1] = '-'

    # Initialize counting array and result array
    count = [0] * (max_index + 1)
    result = [None] * len(arr)

    # Count occurrences of each element
    for i in arr:
        count[int(i[0])] += 1

    # Calculate cumulative counts
    for i in range(1, max_index + 1):
        count[i] += count[i - 1]

    # Build the result array using counting array
    for i in reversed(arr):
        index = int(i[0])
        result[count[index] - 1] = i[1]
        count[index] -= 1

    print(' '.join(result))

    


n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(input().rstrip().split())

countSort(arr)