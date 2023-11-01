n = int(input())

times = []

for _ in range(n):
    x, y = map(int, input().strip().split(" "))
    times.append((x, 1))
    times.append((y, -1))

times.sort()

max_count = 0
count = 0
for i in times:
    count += i[1]

    if max_count < count:
        max_count = count

print(max_count)


