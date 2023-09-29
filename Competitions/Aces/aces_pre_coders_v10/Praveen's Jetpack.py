MOD = 10**9 + 7


def precompute_catalan(max_height):
    catalan_numbers = [0] * (max_height + 1)
    catalan_numbers[0] = 1

    for n in range(1, max_height + 1):
        catalan_numbers[n] = (catalan_numbers[n - 1] * ((4 * n - 2) % MOD) * pow(n + 1, MOD - 2, MOD)) % MOD

    return catalan_numbers

n = int(input())


max_height = 0
test_cases = []
for _ in range(n):
    height = int(input())
    max_height = max(max_height, height)
    test_cases.append(height)


catalan_numbers = precompute_catalan(max_height)


for height in test_cases:
    paths = catalan_numbers[height]
    print(paths)


