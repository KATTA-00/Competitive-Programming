import heapq

def blend_colors(colors, k):
    heap = colors[:]
    heapq.heapify(heap)  # Convert the list into a min-heap
    steps = 0  # Initialize the number of blending steps

    while heap[0] < k:
        if len(heap) < 2:
            return -1
        
        # Blend the two colors with the lowest intensities
        least_intensity = heapq.heappop(heap)
        second_least_intensity = heapq.heappop(heap)
        new_intensity = least_intensity + 2 * second_least_intensity
        heapq.heappush(heap, new_intensity)
        steps += 1 

    return steps


n, k = map(int, input().strip().split())
colors = list(map(int, input().strip().split()))

result = blend_colors(colors, k)
print(result)
