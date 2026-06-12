# Problem Link: https://leetcode.com/problems/palindrome-linked-list/

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        temp = []
        curr_node = head
        while curr_node:
            temp.append(curr_node.val)
            curr_node = curr_node.next
        return temp == temp[::-1]