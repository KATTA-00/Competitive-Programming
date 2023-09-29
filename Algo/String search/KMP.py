# Knuth-Morris-Pratt (KMP) - used for efficient pattern searching in a given text or string

def compute_prefix_array(pattern):
    m = len(pattern)
    prefix_array = [0] * m
    j = 0

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix_array[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix_array[i] = j

    print(prefix_array)
    return prefix_array

def count_occurrences(text, pattern):
    n = len(text)
    m = len(pattern)
    prefix_array = compute_prefix_array(pattern)
    j = 0
    count = 0

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = prefix_array[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            count += 1
            j = prefix_array[j - 1]
            # j=0

    return count

text = input().strip()
pattern = input().strip()
result = count_occurrences(text, pattern)
print(result)