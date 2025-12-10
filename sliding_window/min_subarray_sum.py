"""
LeetCode #209
Minimum size Subarray Sum

Approach:
- Use a dynamic sliding window (two pointers)
- Expand the window by moving the right pointer and adding nums[right]
- Once the window sum reaches or exceeds the target, shrinks it from the left
- Track the minimal window length throughout the process

Time complexity: O(n)
Space Complexity: O(1)
"""
def min_subarray_sum(nums, target):
    left = 0
    right = 0
    current_sum = 0
    min_len = float("inf")
    while right < len(nums):
        current_sum += nums[right]
        right += 1

        while current_sum >= target:
            min_len = min(min_len, right - left)
            current_sum -= nums[left]
            left += 1

    return min_len if min_len != float("inf") else 0