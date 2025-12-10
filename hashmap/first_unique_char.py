"""
First Unique Character in a String
LeetCode #387

Approach:
- Count frequencies of characters in the string using a hash map.
- Second pass: return the first index whose frequency is 1.

Time: O(n)
Space: O(1) = max 26 letters (constant)
"""

def first_unique_char(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    return -1
