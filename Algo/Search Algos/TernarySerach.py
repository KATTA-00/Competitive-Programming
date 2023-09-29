def ternary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        # Calculate mid1 and mid2
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == target:
            return mid1  # Target found at mid1
        elif arr[mid2] == target:
            return mid2  # Target found at mid2

        # If the target is in the left third of the interval
        if target < arr[mid1]:
            right = mid1 - 1
        # If the target is in the right third of the interval
        elif target > arr[mid2]:
            left = mid2 + 1
        # If the target is in the middle third of the interval
        else:
            left = mid1 + 1
            right = mid2 - 1

    return -1  # Target not found

# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7
result = ternary_search(arr, target)
print(result)  # Output: 3 (index of the target element)


'''usage:'''

'''
Problem: Find the Maximum Elevation

Suppose you are given a one-dimensional terrain represented by a function f(x) 
that gives the elevation at each point x. You want to find the highest point (maximum elevation) 
on this terrain within a specified interval [left, right]. 
The terrain is known to be unimodal within the given interval, 
meaning that it increases up to a peak and then decreases.
'''

def ternary_search_max_elevation(elevation_function, left, right, error=1e-9):
    while (right - left) > error:
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3

        if elevation_function(mid1) < elevation_function(mid2):
            left = mid1
        else:
            right = mid2

    # Return the maximum elevation within the specified interval
    return (left + right) / 2, elevation_function((left + right) / 2)

# Example usage:
def terrain_elevation(x):
    # Replace this function with the actual elevation data
    return -(x - 3) ** 2 + 9  # Example terrain (a parabolic hill)

left_boundary = 0
right_boundary = 6
max_elevation_point, max_elevation = ternary_search_max_elevation(terrain_elevation, left_boundary, right_boundary)

print(f"The maximum elevation is {max_elevation} at point {max_elevation_point}")
