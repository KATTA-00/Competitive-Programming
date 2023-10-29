'''
You are given a DNA sequence: a string consisting of characters A, C, G, and T. 
Your task is to find the longest repetition in the sequence. 
This is a maximum-length substring containing only one type of character.

Input

The only input line contains a string of n
 characters.

Output

Print one integer: the length of the longest repetition.

Constraints
    1≤n≤106

Example

Input:
ATTCGGGA

Output:
3
'''


s = str(input().strip())
length = len(s)
count = []
c = 1
if length == 1:
    count.append(1)
for i in range(length-1):
    if s[i] == s[i+1]:
        c += 1
        if i == (length - 2):
           count.append(c) 
    else:
        count.append(c)
        c = 1

print(max(count))
