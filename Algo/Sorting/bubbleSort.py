# def bubble_sort_with_swaps(arr):
#     n = len(arr)
#     swaps_needed = [0] * n
#     cumulative_swaps = [0] * n

#     for i in range(n):
#         for j in range(n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swaps_needed[i] += 1

#     cumulative_swaps[0] = swaps_needed[0]
#     for i in range(1, n):
#         cumulative_swaps[i] = cumulative_swaps[i - 1] + swaps_needed[i]

#     return arr, swaps_needed, cumulative_swaps

# # Example usage:
# arr = [1,2,3,7,5,6,4]
# sorted_arr, swaps_needed, cumulative_swaps = bubble_sort_with_swaps(arr)

# print("Sorted Array:", sorted_arr)
# print("Swaps Needed at Each Step:", swaps_needed)
# print("Cumulative Swaps at Each Step:", cumulative_swaps)

def calculate_cumulative_swaps(arr):
    n = len(arr)
    cumulative_swaps = [0] * n  # Initialize the cumulative swaps array with zeros

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                cumulative_swaps[j] += 1

    return cumulative_swaps

# Example usage:
arr = [1, 2, 3, 7, 5, 6, 4]
cumulative_swaps = calculate_cumulative_swaps(arr)
count = 0
new_array = []

for i in range (1,len(arr)+1):
    index = arr.index(i)
    count += cumulative_swaps[index]
    new_array.append(count)

print("Original array:", arr)
print("Cumulative swaps array:", new_array)




