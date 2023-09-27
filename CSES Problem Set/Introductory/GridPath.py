import math

def move(r, c, ans, steps, reserved):
    if r == n - 1 and c == 0:
        ans += (steps == n * n - 1)
        return

    # if you hit a wall or a path (can only go left or right); return
    if (((r + 1 == n or (visited[r - 1][c] and visited[r + 1][c])) and c - 1 >= 0 and c + 1 < n and not visited[r][c - 1] and not visited[r][c + 1]) or
        ((c + 1 == n or (visited[r][c - 1] and visited[r][c + 1])) and r - 1 >= 0 and r + 1 < n and not visited[r - 1][c] and not visited[r + 1][c]) or
        ((r == 0 or (visited[r + 1][c] and visited[r - 1][c])) and c - 1 >= 0 and c + 1 < n and not visited[r][c - 1] and not visited[r][c + 1]) or
        ((c == 0 or (visited[r][c + 1] and visited[r][c - 1])) and r - 1 >= 0 and r + 1 < n and not visited[r - 1][c] and not visited[r + 1][c])):
        return

    visited[r][c] = True

    if reserved[steps] != -1:
        switch = {
            0: lambda: move(r - 1, c, ans, steps + 1, reserved),
            1: lambda: move(r, c + 1, ans, steps + 1, reserved),
            2: lambda: move(r + 1, c, ans, steps + 1, reserved),
            3: lambda: move(r, c - 1, ans, steps + 1, reserved)
        }
        switch[reserved[steps]]()
        visited[r][c] = False
        return

    # move down
    if r + 1 < n:
        if not visited[r + 1][c]:
            move(r + 1, c, ans, steps + 1, reserved)

    # move right
    if c + 1 < n:
        if not visited[r][c + 1]:
            move(r, c + 1, ans, steps + 1, reserved)

    # move up
    if r - 1 >= 0:
        if not visited[r - 1][c]:
            move(r - 1, c, ans, steps + 1, reserved)

    # move left
    if c - 1 >= 0:
        if not visited[r][c - 1]:
            move(r, c - 1, ans, steps + 1, reserved)

    visited[r][c] = False

def main():
    global visited, n

    n = 7
    visited = [[False] * n for i in range(n)]

    path = input()
    reserved = [-1] * len(path)

    for i in range(len(path)):
        if path[i] == '?':
            reserved[i] = -1
        elif path[i] == 'U':
            reserved[i] = 0
        elif path[i] == 'R':
            reserved[i] = 1
        elif path[i] == 'D':
            reserved[i] = 2
        elif path[i] == 'L':
            reserved[i] = 3

    ans = 0
    steps = 0

    move(0, 0, ans, steps, reserved)

    print(ans)

if __name__ == '__main__':
    main()
