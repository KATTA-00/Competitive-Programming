'''Two Sum:''' #Given an array of integers, 
# find two numbers such that they add up to a specific target
def twoSum(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [nums[left], nums[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []  # No such pair found

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)  # Output: [2, 7]


'''Three Sum''' 
#Given an array of integers,
# find all unique triplets in the array that sum up to a specific target.

def threeSum(nums):
    nums.sort()  # Sort the array first
    triplets = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates

        left, right = i + 1, len(nums) - 1
        target = -nums[i]

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                triplets.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1  # Skip duplicates
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1  # Skip duplicates
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return triplets

# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
result = threeSum(nums)
print(result)  # Output: [[-1, -1, 2], [-1, 0, 1]]




'''Subarray with Given Sum:''' #Given an array of positive integers and a target sum, 
# find the contiguous subarray that adds up to the target sum.

def subarraySum(nums, target):
    sum_map = {}
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num

        if current_sum == target:
            count += 1

        if current_sum - target in sum_map:
            count += sum_map[current_sum - target]

        if current_sum in sum_map:
            sum_map[current_sum] += 1
        else:
            sum_map[current_sum] = 1

    return count

# Example usage:
nums = [1, 2, 3, 4, 5]
target = 9
result = subarraySum(nums, target)
print(result)  # Output: 2


# Cycle Detection in Linked Lists: Determine 
# if a linked list has a cycle and find the starting point of the cycle.

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

# Example usage:
# Create a linked list with a cycle
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = head.next  # Create a cycle

result = hasCycle(head)
print(result)  # Output: True
