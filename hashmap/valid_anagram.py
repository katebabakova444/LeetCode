"""
LeetCode #242
Valid Anagram

Approach:
- Count character frequencies in the first string
- Decrease frequencies using the second string
- If all counts return to zero - the strings are anagrams

Time Complexity: O(n)
Space Complexity: O(1)
"""

def is_anagram(s, t):
    if len(s) != len(t):
        return False

    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False
    return True

