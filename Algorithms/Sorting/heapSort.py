'''
use Heap Sort when you need to sort a large dataset, and you want a stable and efficient sorting algorithm 
with a consistent time complexity of O(n log n) in the worst-case scenario. Heap Sort is often used in 
scenarios where you cannot afford the additional memory usage of algorithms like Merge Sort or QuickSort.
'''


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap root (max element) with the last element
        heapify(arr, i, 0)  # Heapify the reduced heap

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
print("Sorted array:", arr)