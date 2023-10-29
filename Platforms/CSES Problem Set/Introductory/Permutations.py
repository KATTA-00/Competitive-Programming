n = int(input())

if n == 1:
    print(1)
if n <= 3:
    # For n <= 2, a beautiful permutation is not possible
    print("NO SOLUTION")
else:
    beautiful_permutation = []

    # Initialize a list with values from 1 to n
    permutation = list(range(1, n + 1))

    # Iterate through the odd indices and append them to the beautiful_permutation
    for i in range(1, n, 2):
        beautiful_permutation.append(permutation[i])


    # Iterate through the even indices and append them to the beautiful_permutation
    for i in range(0, n, 2):
        beautiful_permutation.append(permutation[i])

    # Print the beautiful permutation
    out = list(map(str,beautiful_permutation))
    print(' '.join(out))