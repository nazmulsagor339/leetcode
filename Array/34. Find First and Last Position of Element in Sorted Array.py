# Problem Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution(object):
    def searchRange(self, nums, target):
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]
        left, right = 0, len(nums)-1
        while left <= right:
            middle = (left + right)//2
            if nums[middle] > target:
                right = middle - 1
            if nums[middle] < target:
                left = middle + 1
            if nums[middle] == target:
                first, last = middle, middle
                while first-1 >= 0 and nums[first-1] == target:
                    first -= 1
                while last+1 < len(nums) and nums[last+1] == target:
                    last += 1
                return [first, last]
        return [-1, -1]
