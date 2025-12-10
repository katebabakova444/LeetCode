# Sliding Window Pattern

### Sliding windows allow:

- Reducing complexity from O(n²) to **O(n)**
- Working with **fixed-size windows** (e.g., length = 3)
- Working with **dynamic windows** that expand or contract based on conditions
- Maintaining running values (sum, distinct characters, counts)
- Efficiently validating substrings or subarrays without recomputing everything

---

### Typical problems:

- Substrings of Size Three with Distinct Characters  
- Minimum Size Subarray Sum  
- Maximum Average Subarray  
- Longest Substring Without Repeating Characters  
- Permutation in String  
- Find All Anagrams in a String  

---

### Complexity:

- **Time:** O(n) — each index is visited at most twice  
- **Space:** O(1) or O(k), depending on whether the window tracks extra information  

---

Solutions in this folder demonstrate how this technique helps process parts of arrays and strings efficiently by moving the window instead of recalculating everything from scratch.