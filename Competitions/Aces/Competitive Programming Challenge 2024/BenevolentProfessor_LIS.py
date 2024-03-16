from bisect import bisect_right

# Input: Number of students (N) and number of classes (K)
n, k = map(int, input().split())

# Initialize array to store ranks of students
student_ranks = [0] * (n + 1)
INFINITY = 10**5 + 1

# Input: Student ranks and classes
for _ in range(n):
    class_num, rank = map(int, input().split())
    # Reverse the ranks to easily handle ranks in descending order
    student_ranks[n - rank] = class_num

# LIS (Longest Increasing Subsequence) calculation
lis = [INFINITY] * (n + 1)
lis[0] = -INFINITY

for i in range(n):
    # Binary search to find the position where current student's rank can be inserted
    insertion_point = bisect_right(lis, student_ranks[i])
    if lis[insertion_point - 1] <= student_ranks[i] <= lis[insertion_point]:
        lis[insertion_point] = student_ranks[i]

# Find the length of the LIS
min_exams = 0
for i in range(1, n + 1):
    if lis[i] < INFINITY:
        min_exams = i

# Output: Minimum number of exams needed
print(min_exams)