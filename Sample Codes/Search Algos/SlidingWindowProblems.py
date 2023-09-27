# Given an array of integers and an integer k, find the 
# maximum sum of any contiguous subarray of size k.

def maxSumSubarray(nums, k):
    window_sum = sum(nums[:k])  # Calculate initial sum for the first window
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]  # Slide the window by adding the next element and removing the first element

        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum

# Example usage:
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
result = maxSumSubarray(nums, k)
print(result)  # Output: 16 (maximum sum of a subarray of size 3)



#############################################################################

# Given an array of positive integers and a positive integer target, find the minimum 
# length of a contiguous subarray whose sum is greater than or equal to the target.

def minSubarrayLen(target, nums):
    left, right = 0, 0
    current_sum = 0
    min_length = float('inf')

    while right < len(nums):
        current_sum += nums[right]
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
        right += 1

    return min_length if min_length != float('inf') else 0

# Example usage:
nums = [2, 3, 1, 2, 4, 3]
target = 7
result = minSubarrayLen(target, nums)
print(result)  # Output: 2 (minimum subarray [4, 3])
