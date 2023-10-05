num1 = int(input())
s1 = list(input())
num2 = int(input())
s2 = list(input())

import collections

result = collections.Counter(s1) & collections.Counter(s2)

intersected_list = list(result.elements())

print(len(intersected_list))