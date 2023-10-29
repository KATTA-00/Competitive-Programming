'''
You are given all numbers between 1,2,…,n except one. 
Your task is to find the missing number.

Input

The first input line contains an integer n.

The second line contains n−1 numbers. Each number is distinct and between 1 and n (inclusive).

Output

Print the missing number.

Constraints
    2≤n≤2⋅105

Example

Input:
5
2 3 1 5

Output:
4

'''


n = int(input())

numList = list(map(int,input().split()))

numList.sort()

for i in range (1,n+1):
    if i == n:
       print(i)
       break 
    elif i != numList[i-1]:
        print(i)
        break
