"""
LeetCode #217
Contains Duplicate

Approach:
-Return True if the input list contains any duplicate values.
-Uses hash set to track seen elements.

Time complexity: O(n)
Space complexity: O(n)
"""

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False