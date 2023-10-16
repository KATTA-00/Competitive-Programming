n = int(input())

class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

node_dict = {}

def add_node(parent_name, child_name):
    parent = node_dict[parent_name]
    child = Node(child_name)
    child.parent = parent
    parent.children.append(child)
    node_dict[child_name] = child

def remove_node(node_name):
    node = node_dict[node_name]
    parent = node.parent
    parent.children.remove(node)
    del node_dict[node_name]

def find_kth_upstream(node_name, k):
    node = node_dict.get(node_name)
    if not node:
        return "None"
    for _ in range(k):
        if node.parent:
            node = node.parent
        else:
            return "None"
    return node.name

node_dict["ROOT"] = Node("ROOT")

for _ in range(n):
    t1, t2 = input().strip().split()
    add_node(t2, t1)

num = int(input())

for _ in range(num):
    ss = input()
    if ss.startswith("N"):
        _, t1, t2 = ss.split()
        add_node(t1, t2)
    elif ss.startswith("R"):
        _, t1 = ss.split()
        remove_node(t1)
    else:
        _, t1, t2 = ss.split()
        t2 = int(t2)
        result = find_kth_upstream(t1, t2)
        print(result)
