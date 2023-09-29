# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

def get_min_moves(start, end, n):
    q = deque([(start, 0)])
    visited = {start}

    while q:

        coord, dist = q.popleft()

        i, j = coord
        
        next_coords = [
            (i + 1, j + 2), (i + 2, j + 1),
            (i + 1, j - 2), (i + 2, j - 1),
            (i - 1, j + 2), (i - 2, j + 1),
            (i - 1, j - 2), (i - 2, j - 1),
        ]

        for ni, nj in next_coords:

            if 0 <= ni < n and 0 <= nj < n:

                if (ni, nj) in visited:
                    continue

                if ni == end[0] and nj == end[1]:
                    return dist
                
                q.append(((ni, nj), dist + 1))
                visited.add((ni, nj))    
                
    return -1 

n = int(input())
start = [int(i) for i in input().strip("()").split(",")]
end = [int(i) for i in input().strip("()").split(",")]

print(get_min_moves(tuple(start), tuple(end), n))