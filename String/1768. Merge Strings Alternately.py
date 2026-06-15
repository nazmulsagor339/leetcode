# Problem Link: https://leetcode.com/problems/merge-strings-alternately/

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n = 0
        merged = ''
        while n < len(word1) and n < len(word2):
            merged += word1[n]
            merged += word2[n]
            n += 1
        if n < len(word1):
            merged += word1[n:]
        if n < len(word2):
            merged += word2[n:]
        return merged