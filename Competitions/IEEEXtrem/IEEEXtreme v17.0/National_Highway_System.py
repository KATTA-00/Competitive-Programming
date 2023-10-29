class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y

def minHighwayCost(n, roads):
    city_indices = {}
    index_counter = 0

    def get_index(city_name):
        nonlocal index_counter
        if city_name not in city_indices:
            city_indices[city_name] = index_counter
            index_counter += 1
        return city_indices[city_name]

    for i in range(n):
        city1, city2, cost = roads[i]
        roads[i] = (get_index(city1), get_index(city2), cost)

    roads.sort(key=lambda x: x[2])  # Sort roads by cost
    mst_cost = 0
    selected_roads = []
    dsu = DisjointSet(index_counter)

    for road in roads:
        city1, city2, cost = road

        if dsu.find(city1) != dsu.find(city2):
            dsu.union(city1, city2)
            mst_cost += cost
            selected_roads.append(road)

    if len(selected_roads) == index_counter - 1:
        return mst_cost
    else:
        return -1

n = int(input())
roads = []

for _ in range(n):
    city1, city2, cost = input().split()
    cost = int(cost)
    roads.append((city1, city2, cost))

result = minHighwayCost(n, roads)
print(result)
