# Problem: https://leetcode.com/problems/two-sum/description/
# Problem Statement: Given an array of integers nums and an integer target,
        # return indices of the two numbers such that they add up to target.
# Explanation: We can use a hash map to store the numbers we have seen so far
            # and their corresponding indices. For each number, we check if the
            # complement (target - current number) exists in the hash map. If it does, 
            # we have found our pair and can return their indices. If not, 
            # we add the current number and its index to the hash map for future reference.
# Time Complexity: O(n) - We traverse the list of numbers once.

class Solution(object):
    def twoSum(self, nums, target):
        findPair = {}
        for i, num in enumerate(nums):
            value = target - num
            if value in findPair:
                return [i,findPair[value]]
            findPair[num] = i