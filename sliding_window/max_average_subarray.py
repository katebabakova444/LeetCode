"""
LeetCode #643
Maximum Average Subarray
Approach:
- Sliding window (fixed size)
- Compute the sum of the first k elements.
- Slide the window one position at a time
- Track the maximum window sum
- Return maximum average

Time complexity: O(n)
Space Complexity: O(1)
"""
def max_average(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum / k

