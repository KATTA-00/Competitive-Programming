n = int(input())
import os
groups = []

for _ in range(n):
    s = input().strip().split(" ")[1:]
    groups.append(s)

m = int(input())

# print(groups)
for _ in range(m):

    a, b = input().strip().split(" ")

    ini_strlist = []
    ini_strlist.append(a)
    ini_strlist.append(b)
    start = len(os.path.commonprefix(ini_strlist))

    ini_strlist = []
    ini_strlist.append(a[::-1])
    ini_strlist.append(b[::-1])
    end = len(os.path.commonprefix(ini_strlist))

    if start == 0 and end == 0:
        print("OK")
        continue
    else:
        print("REJECT")


    # print(a[start:len(a) - end])

##################################################################################################

n = int(input())
groups = []

for _ in range(n):
    s = input().strip().split(" ")[1:]
    groups.append(s)

m = int(input())

def replace_words(word, groups, memo):
    if word in memo:
        return memo[word]

    for group in groups:
        for group_word in group:
            if group_word in word:
                word = word.replace(group_word, group[0])

    memo[word] = word
    return word

for _ in range(m):
    a, b = input().strip().split(" ")

    memo = {}  # Memoization dictionary for word replacements
    a_replaced = replace_words(a, groups, memo)
    b_replaced = replace_words(b, groups, memo)

    if a_replaced == b_replaced:
        print("REJECT")
    else:
        print("OK")
