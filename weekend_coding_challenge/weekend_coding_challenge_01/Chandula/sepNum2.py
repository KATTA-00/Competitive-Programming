def separateNumbers(s):
    n = len(s)
    for length in range(1, n // 2 + 1):
        first_num = int(s[:length])
        current_num = first_num
        current_pos = length

        while current_pos < n:
            current_num += 1
            current_str = str(current_num)
            if not s.startswith(current_str, current_pos):
                break
            current_pos += len(current_str)

        if current_pos == n:
            print("YES", first_num)
            return

    print("NO")

n = int(input().strip())
for i in range(n):
    s = input().strip()
    separateNumbers(s)