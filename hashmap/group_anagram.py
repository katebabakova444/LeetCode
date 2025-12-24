"""
Group Anagram
LeetCode #49

Approach:
- Create a dictionary where the key is the sorted version of the word.
- Add the word to the list of its anagram group.
- Return all values.

Time Complexity: O(n * k log k) where n - number of words, k = length of each word
Space Complexity: O(n)

"""

def group_anagram(s):
    group = {}
    for word in s:
        sorted_word = "".join(sorted(word))
        if sorted_word not in group:
            group[sorted_word] = []
        group[sorted_word].append(word)
    return list(group.values())
