class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = []
        left = len(nums1)
        right = len(nums2)
        i, j = 0, 0
        while i<left and j<right:
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i +=1
            elif nums1[i] >= nums2[j]:
                nums3.append(nums2[j])
                j +=1
        if i < left:
            nums3 += nums1[i:]
        if j < right:
            nums3 += nums2[j:]
        if len(nums3)%2 != 0:
            index = len(nums3)//2
            return float(nums3[index])
        else:
            index = len(nums3)//2
            return float(nums3[index-1] + nums3[index])/2