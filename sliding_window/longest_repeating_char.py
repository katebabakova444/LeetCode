"""
LeetCode #424
Longest repeating character replacement

Approach:
- Use sliding window with two pointers
- Use hash map to store the frequency of characters in the current window
- Expand the window by moving the right pointer
- If character appears more than once, shrink the window from the left
- Track the maximum window size during the process

Time Complexity: O(n)
Space Complexity: O(n) (or O(1) with fixed alphabet assumption)
"""

def character_replacement(s, k):
    left = 0
    count = {}
    max_freq = 0
    max_len = 0
    for right in range(len(s)):
        char = s[right]
        count[char] = count.get(char, 0) + 1
        max_freq = max(max_freq, count[char])

        window_size = right - left + 1
        while window_size - max_freq > k:
            count[s[left]] -= 1
            left += 1
        max_len = max(max_len, window_size)

    return max_len
