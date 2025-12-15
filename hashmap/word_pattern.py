"""
LeetCode #290
Word Pattern

Approach:
- Split the string 's' into words
- If lengths are different, return False
- Use two hash maps:
     * char_ro_word
     * word_to_char
- Validate mappings in both directions to ensure one-to-one mapping

Time Complexity: O(n)
Space Complexity: O(n)
"""
def word_pattern(pattern, s):
    s = s.split()
    if len(s) != len(pattern):
        return False
    char_to_word = {}
    word_to_char = {}
    for char, word in zip(pattern, s):
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
            else:
                char_to_word[char] = word
        if word in word_to_char:
            if word_to_char[word] != char:
                return False
            else:
                word_to_char[word] = char
    return True

