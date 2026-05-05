# LeetCode Solutions in Python

This repository contains my solutions to problems from [LeetCode]([https://leetcode.com/](https://leetcode.com/u/nazmulsagor339/) implemented in Python. The goal of this repo is to improve problem-solving skills, master data structures & algorithms, and prepare for technical interviews.

---

## About

-  Language: Python
-  Platform: LeetCode
-  Focus:
  - Data Structures
  - Algorithms
  - Coding Interview Preparation

---
##  Example Solution Format

Each solution typically includes:

- Problem link
- Problem description (short)
- Approach/Explanation
- Time & Space Complexity
- Python implementation

```python
# Example: Two Sum

class Solution(object):
    def twoSum(self, nums, target):
        findPair = {}
        for i, num in enumerate(nums):
            value = target - num
            if value in findPair:
                return [i,findPair[value]]
            findPair[num] = i
