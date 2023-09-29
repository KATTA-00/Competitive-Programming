'''
searching algorithm designed to search for a specific element in 
a sorted array by dividing the array into subarrays of exponentially increasing 
size and then performing binary search within these subarrays. It is especially 
useful when you don't have information about the array size in advance.
'''

def exponential_search(arr, target):
    n = len(arr)
    
    if arr[0] == target:
        return 0  # Target is the first element

    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    # Perform binary search within the range [i/2, min(i, n-1)]
    left, right = i // 2, min(i, n - 1)
    
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = exponential_search(arr, target)
print(result)  # Output: 4 (index of the target element)
