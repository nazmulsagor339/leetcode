# Problem link: https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        # return if the string list is empty
        if len(strs) == 0:
            return ""
        temp = ""
        # loop through the first string and compare it 
        # with the rest of the strings in the list
        for i in range(len(strs[0])):
            # loop through the rest of the strings in the list
            for j in range(1,len(strs)):
                # if the index is out of range for the current string
                #  or the characters do not match, 
                # return the common prefix found so far
                if i == len(strs[j]) or strs[0][i] != strs[j][i]:
                    return temp
            temp += strs[0][i]
        return temp
        