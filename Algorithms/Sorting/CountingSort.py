'''
Counting Sort works by counting the frequency of each element in the 
input array and then placing the elements in sorted order based on their counts.
'''

def countingSort(arr):
    # Find the minimum and maximum values in the input array
    min_val, max_val = min(arr), max(arr)
    
    # Create a count array to store the frequencies of elements
    count = [0] * (max_val - min_val + 1)
    
    # Count the frequencies of elements in the input array
    for num in arr:
        count[num - min_val] += 1
    
    # Build the sorted array based on the counts
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i + min_val] * count[i])
    print(count)
    return sorted_arr

# Example usage:
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = countingSort(arr)
print("Sorted array:", sorted_arr)

# [1, 2, 2, 1, 0, 0, 0, 1]
# Sorted array: [1, 2, 2, 3, 3, 4, 8]


