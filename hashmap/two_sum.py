"""
LeetCode #1
Two sum

Approach:
- Return indices of the two numbers in 'nums' that add up to 'target'.
- Uses a hash map to store previously seen numbers for O(n) time complexity.
- Assumes exactly one valid solution exists.

Time complexity: O(n)
Space complexity: O(n)
"""

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]

        seen[num] = i
