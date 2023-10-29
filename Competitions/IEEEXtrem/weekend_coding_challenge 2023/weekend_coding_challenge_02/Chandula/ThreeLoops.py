def count_tuples(n, target_sum):
    count = 0

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            c = target_sum - a - b
            if 1 <= c <= n:
                count += 1

    return count


n,sum = map(int,input().split())
print(count_tuples(n, sum))


