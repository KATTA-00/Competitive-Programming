from itertools import permutations
from itertools import combinations

def generate_strings(s):
    # perms = set(permutations(s))
    perms = set(permutations(s, 4)) # if i want length 4 strings
    sorted_perms = sorted([''.join(p) for p in perms])
    return sorted_perms



##############################
def generate_combinations(s):
    combs = set(combinations(s, 4))
    sorted_combs = sorted([''.join(c) for c in combs])
    return sorted_combs


#############################

s = input().strip()
result1 = generate_combinations(s)
result = generate_strings(s)

print(len(result))
for string in result:
    print(string)
