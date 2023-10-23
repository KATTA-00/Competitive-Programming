a, b, t = list(map(int, input().strip().split(" ")))

point_a = []
point_b = []


for _ in range(a):
    x, y = list(map(int, input().strip().split(" ")))
    point_a.append((x, y))
    
for _ in range(b):
    x, y = list(map(int, input().strip().split(" ")))
    point_a.append((x, y))
    
class Node:
    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right

def build_kd_tree(points, depth=0):
    if not points:
        return None

    k = len(points[0])
    axis = depth % k

    points.sort(key=lambda x: x[axis])
    median = len(points) // 2

    return Node(
        point=points[median],
        left=build_kd_tree(points[:median], depth + 1),
        right=build_kd_tree(points[median + 1 :], depth + 1)
    )

def find_nearest_neighbors(root, point, depth=0, best=None):
    if root is None:
        return best

    k = len(point)
    axis = depth % k

    next_best = None
    next_branch = None

    if best is None or sum((point[axis] - best.point[axis]) ** 2 for axis in range(k)) > (point[axis] - root.point[axis]) ** 2:
        next_best = root
    else:
        next_branch = root.left if point[axis] < root.point[axis] else root.right

    if next_branch is not None:
        next_best = find_nearest_neighbors(next_branch, point, depth + 1, next_best)

    return next_best

def find_nearest_pairs(A, B):
    root_A = build_kd_tree(A)
    root_B = build_kd_tree(B)

    nearest_pairs = []

    for point_B in B:
        nearest_A = find_nearest_neighbors(root_A, point_B)
        if find_nearest_neighbors(root_B, nearest_A.point) == point_B:
            nearest_pairs.append((nearest_A.point, point_B))

    return nearest_pairs


nearest_pairs = find_nearest_pairs(point_a, point_b)

for pair in nearest_pairs:
    print("Pair:", pair[0], pair[1])



