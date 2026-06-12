# Problem Link: https://leetcode.com/problems/middle-of-the-linked-list/

class Solution(object):
    def middleNode(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow