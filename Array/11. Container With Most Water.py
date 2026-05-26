# Problem Link: https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height)-1
        container = 0
        while left<right:
            if height[left] < height[right]:
                temp = height[left] * (right - left) # calculating the area of the container
                if temp > container: # Updating container for the maximum area
                    container = temp
                left += 1
            elif height[left] >= height[right]:
                temp = height[right] * (right - left) # calculating the area of the container
                if temp > container:
                    container = temp
                right -= 1
        return container