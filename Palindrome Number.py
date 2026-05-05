# Problem: https://leetcode.com/problems/palindrome-number/description/
# Problem Statement: Given an integer x, return true if x is a palindrome, and false otherwise.
# Explanation: We can convert the integer to a list of its digits and check if the list
            # is the same as its reverse. If it is, then the number is a palindrome.
# Time Complexity: O(n) - We need to traverse the digits of the number once.

class Solution(object):
    def isPalindrome(self, x):
        checkPalindrome = []
        if x<0:
            return False
        else:
            while x != 0:
                rem = x % 10
                checkPalindrome.append(rem)
                div = x // 10
                x = div
            if checkPalindrome == checkPalindrome[::-1]:
                return True
            else:
                return False