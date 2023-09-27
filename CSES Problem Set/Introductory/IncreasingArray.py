'''
You are given an array of n integers. 
You want to modify the array so that it is increasing, i.e., every element is at least as large as the previous element.

On each move, you may increase the value of any element by one. What is the minimum number of moves required?

Input

The first input line contains an integer n: the size of the array.

Then, the second line contains n integers x1,x2,…,xn : the contents of the array.

Output

Print the minimum number of moves.

Constraints
    1 ≤ n ≤ 2*10**5
    1 ≤ xi ≤ 10**9

Example

Input:
5
3 2 5 1 7

Output:
5

'''


n=int(input().strip())

arr=list(map(int,input().split()))

Count=0

for i in range(1,len(arr)):
    if arr[i-1]>arr[i]:
        Count+=arr[i-1]-arr[i]
        arr[i]=arr[i-1]

print(Count)


# n = int(input().strip())

# arr = list(map(int, input().rstrip().split()))
# cArr = []
# length = n
# count = 0
# print()
# for i in range(1,length):
#     key = arr[i]
#     ind = i-1
#     while ind>=0 and arr[ind]>key:
#         arr[ind+1]=arr[ind]
#         ind-=1
#         count += 1
#         out = list(map(str,arr))
#         out[ind+1] = str(key)
#         print(' '.join(out))
#     arr[ind+1] = key
    
# print(count)