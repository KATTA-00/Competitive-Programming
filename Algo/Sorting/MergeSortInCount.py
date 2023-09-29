from collections import deque


def countInversions(arr):
    arr, count = mergeSort(arr)
    return count
    
    
def mergeSort(arr):
    def merge(left, right):
        result = []
        count = 0  # Initialize inversion count

        left_idx, right_idx = 0, 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1
                count += len(left) - left_idx  # Count inversions

        result.extend(left[left_idx:])
        result.extend(right[right_idx:])

        return result, count

    if len(arr) <= 1:
        return arr, 0  # Return the array and initial inversion count (0)

    mid = len(arr) // 2
    left, left_count = mergeSort(arr[:mid])
    right, right_count = mergeSort(arr[mid:])
    merged, merge_count = merge(left, right)

    # Combine inversion counts from the left, right, and merge steps
    total_count = left_count + right_count + merge_count

    return merged, total_count


def mergeSort2(arr):
    def merge(left, right):
        result = []
        count = 0  # Initialize inversion count

        left, right = deque(left), deque(right)

        while left and right:
            if left[0] <= right[0]:
                result.append(left.popleft())
            else:
                result.append(right.popleft())
                count += len(left)  # Increment inversion count

        result.extend(left)
        result.extend(right)

        return result, count

    if len(arr) <= 1:
        return arr, 0  # Return the array and initial inversion count (0)

    mid = len(arr) // 2
    left, left_count = mergeSort(arr[:mid])
    right, right_count = mergeSort(arr[mid:])
    merged, merge_count = merge(left, right)

    # Combine inversion counts from the left, right, and merge steps
    total_count = left_count + right_count + merge_count

    return merged, total_count




t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    print(countInversions(arr))


    