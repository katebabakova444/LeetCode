"""
LeetCode #3
Longest Substring Without Repeating Characters

Approach:
- Sliding widow
- Use a set to track unique characters in the current window
- Expand the window by moving the right pointer
- If duplicate character appears, shrink the window from the left
  until the substring becomes valid again.
- Track the maximum window length during the process.
Time Complexity: O(n)
Space Complexity: O(min(n, m)) # n = length of string, m = charset size
"""
def longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[left] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length
