"""
LeetCode #1876
Substrings of Size Three with Distinct Characters

Approach:
- Use a fixed-size sliding window of length 3
- Move the window from left to right
- Convert each window to a set and check if it contains 3 distinct chars

Time Complexity: O(n)
Space Complexity: O(1)


"""
def find_substrings(s):
    window_size = 3
    left = 0
    count = 0
    for left in range(len(s) - window_size):
        right = left + window_size - 1
        window = s[left:right + 1]
        if len(set(window)) == 3:
            count += 1
    return count