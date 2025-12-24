"""
Top K Frequent Elements
LeetCode #347

Approach:
- Count frequency of each number using a dictionary.
- Sort the dictionary items by frequency in descending order.
- Extract first K numbers.

Time Complexity: O(n log n) - sorting the frequency map.
Space Complexity: O(n) - storing frequencies.
"""

def topKFrequent(nums, k):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    sorted_count = sorted(count, key=lambda x:count[x], reverse=True)
    return sorted_count[:k]