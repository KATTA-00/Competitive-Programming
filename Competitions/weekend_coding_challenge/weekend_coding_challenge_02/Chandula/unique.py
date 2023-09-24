# def find_substrings(input_string):
#     substrings = []
#     n = len(input_string)

#     for length in range(1, n + 1):
#         for i in range(n - length + 1):
#             substrings.append(input_string[i:i+length])

#     return substrings

# print(len(find_substrings("xxyz")))
# print(len(set(find_substrings("xxyz"))))




# def min_changes_to_distinct_substrings(N, S):
#     # Check if the number of substrings (N*(N+1)/2) is greater than the number of unique substrings
#     if N * (N + 1) // 2 <= len(set(S)):
#         return 0  # All substrings are already distinct, no changes needed

#     # Otherwise, find the minimum number of changes required to make all substrings distinct
#     char_count = [0] * 26  # Array to count the occurrences of each lowercase letter

#     changes_needed = 0
#     for i in range(N):
#         char_count[ord(S[i]) - ord('a')] += 1
#         if char_count[ord(S[i]) - ord('a')] > 1:
#             changes_needed += 1

#     return changes_needed + 1  # Add 1 for the main diagonal

# # Input
# T = int(input())  # Number of test cases
# for _ in range(T):
#     N = int(input())  # Length of the string
#     S = input()       # The string itself

#     # Calculate and print the result
#     result = min_changes_to_distinct_substrings(N, S)
#     print(result)

t=int(input())

def answer(arr,n):
    all=list(dict.fromkeys(list(arr)))
    # print(all)
    if len(all)==26:
        return -1
    if len(arr)==len(all):
        return 0
    return len(arr)-len(all)
    
    

for _ in range(t):
    n=int(input())
    arr=input()
    print(answer(arr,n))
    