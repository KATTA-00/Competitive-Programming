from cmath import inf
10
def closestNumbers(arr):
    arr.sort()
    print(arr)
    min = inf
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] < min:
            minArr = [arr[i],arr[i+1]]
            min = arr[i+1] - arr[i]
        elif arr[i+1] - arr[i] == min:
            minArr.append(arr[i])
            minArr.append(arr[i+1])

    return minArr

n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
answer = closestNumbers(arr)
print(' '.join(map(str, answer)))

# function to extract subset which have n elements and which gives minimum difference between each elements of it, from the given array
# array and value 'n' get as inputs
# optimized solution
def get_subset(arr, n):
    # sort the array
    arr.sort()
    # initialize the minimum difference
    min_diff = float('inf')
    # initialize the result
    result = []
    # loop through the array
    for i in range(len(arr)-n+1):
        # check the difference between the last element and the first element of the subset
        diff = arr[i+n-1] - arr[i]
        # if the difference is less than the minimum difference
        if diff < min_diff:
            # update the minimum difference
            min_diff = diff
            # update the result
            result = arr[i:i+n]
    # return the result
    return result