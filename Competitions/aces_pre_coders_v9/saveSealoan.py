import heapq

def min_travel_time(n, m, k, planets, routes):
    # Initialize a list to keep track of collected stones for each planet
    collected_stones = [set() for _ in range(n)]
    
    for i in range(n):
        for stone in planets[i]:
            collected_stones[i].add(stone)
    
    # Create a memoization table to store the minimum time
    memo = [[float('inf')] * (k + 1) for _ in range(n)]
    
    # Initialize the starting planet
    memo[0][len(collected_stones[0])] = 0
    
    # Create a priority queue for Dijkstra's algorithm
    pq = [(0, 0, set(collected_stones[0]))]  # (time, planet, collected_stones)
    
    while pq:
        time, planet, collected = heapq.heappop(pq)
        
        if planet == n - 1 and len(collected) == k:
            return time
        
        for neighbor, travel_time in routes[planet]:
            next_collected = collected.union(collected_stones[neighbor])
            next_time = time + travel_time
            
            if next_time < memo[neighbor][len(next_collected)]:
                memo[neighbor][len(next_collected)] = next_time
                heapq.heappush(pq, (next_time, neighbor, next_collected))
    
    return -1

def main():
    n, m, k = map(int, input().split())
    planets = []
    routes = [[] for _ in range(n)]

    for i in range(n):
        planet_info = list(map(int, input().split()))
        planets.append(planet_info[1:])
    
    for _ in range(m):
        u, v, t = map(int, input().split())
        routes[u - 1].append((v - 1, t))
        routes[v - 1].append((u - 1, t))

    result = min_travel_time(n, m, k, planets, routes)
    print(result)

if __name__ == "__main__":
    main()
