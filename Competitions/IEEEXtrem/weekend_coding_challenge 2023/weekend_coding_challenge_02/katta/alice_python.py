from queue import Queue

MAXN = 5005
INF = 10000000

n, m = map(int, input().split())
adjMatrix = [[INF for _ in range(MAXN)] for _ in range(MAXN)]
qq = [0] * MAXN
res = [0] * MAXN

front = None
rear = None

class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

def Enqueue(x):
    global front, rear
    temp = Node(x)
    temp.next = None
    if front is None and rear is None:
        front = rear = temp
        return
    rear.next = temp
    rear = temp

def Dequeue():
    global front, rear
    temp = front
    if front is None:
        return
    if front == rear:
        front = rear = None
    else:
        front = front.next
    del temp

def Front():
    global front
    if front is None:
        return -1
    return front.data

def reset():
    global front, rear
    front = None
    rear = None

dist = [0] * MAXN

def bfs(src):
    global front, rear
    reset()

    for i in range(MAXN):
        dist[i] = INF

    dist[src] = 0

    Enqueue(src)

    while front is not None:
        u = Front()
        Dequeue()

        for i in range(1, n + 1):
            if dist[i] > dist[u] + adjMatrix[u][i]:
                dist[i] = dist[u] + adjMatrix[u][i]
                Enqueue(i)

for u in range(MAXN):
    for v in range(MAXN):
        adjMatrix[u][v] = INF

for i in range(m):
    u, v, w = map(int, input().split())
    adjMatrix[v][u] = min(adjMatrix[v][u], w)

d, q = map(int, input().split())
qq = list(map(int, input().split()))

bfs(d)

for i in range(q):
    res[i] = dist[qq[i]]

for i in range(q):
    if res[i] == INF:
        print("Impossible")
    else:
        print(res[i])