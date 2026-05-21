# Problem link: https://leetcode.com/problems/sort-an-array/

# Approach1: Merge Sort
class Solution(object):
    def sortArray(self, nums):
        def merge_arr(left,right):
            result = []
            l,r=len(left),len(right)
            i,j=0,0
            while i<l and j<r:
                if left[i]<=right[j]:
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j+=1
            if i<l:
                while i<l:
                    result.append(left[i]) 
                    i+=1
            if j<r:
                while j<r:
                    result.append(right[j])
                    j+=1
            return result
        def arr_divide(nums):
            if len(nums)<=1:
                return nums
            mid = len(nums) // 2
            left_arr = nums[:mid]
            right_arr = nums[mid:]
            left = arr_divide(left_arr)
            right = arr_divide(right_arr)
            return merge_arr(left, right)
        return arr_divide(nums)

