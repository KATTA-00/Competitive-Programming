def preprocess_string(s):
    t = '#'.join('^{}$'.format(s))
    return t

s = input()

t = preprocess_string(s)

n = len(t)
p = [0] * n 
center, right = 0, 0

for i in range(1, n - 1):
    if i < right:
        mirror = 2 * center - i
        p[i] = min(right - i, p[mirror])


    while t[i + p[i] + 1] == t[i - p[i] - 1]:
        p[i] += 1

    if i + p[i] > right:
        center, right = i, i + p[i]

max_len = max(p)
max_index = p.index(max_len)

start = (max_index - max_len) // 2
end = start + max_len
print(s[start:end]) 

