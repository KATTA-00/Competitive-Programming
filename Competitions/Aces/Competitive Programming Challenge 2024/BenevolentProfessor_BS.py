# Input: Number of students (N) and number of classes (K)
n, k = list(map(int, input().strip().split()))

# Initialize array to store students' ranks and classes
student_data = [None] * n

# Input: Student ranks and classes
for _ in range(n):
    class_num, rank = list(map(int, input().strip().split()))
    # Store student's class in an array based on their rank
    student_data[rank - 1] = class_num

# Initialize list to store sequence of exams
exams = []

# Construct sequence of exams
for student_class in student_data:
    # Use binary search to find the appropriate position to insert the current student into the exam sequence
    lo, hi = 0, len(exams)
    while lo < hi:
        mid = (lo + hi) // 2
        if student_class <= exams[mid][-1]:
            lo = mid + 1
        else:
            hi = mid
    # If the student belongs to a new exam, add a new exam to the sequence
    if hi == len(exams):
        exams.append([student_class])
    # Otherwise, append the student to an existing exam
    else:
        exams[lo].append(student_class)

# Output: Minimum number of exams needed
print(len(exams))