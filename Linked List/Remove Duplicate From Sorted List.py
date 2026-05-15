# Problem link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        test = head
        prev = head
        dummy = set()
        while test:
            if test.val in dummy:
                prev.next = test.next
                test = test.next
            else:
                dummy.add(test.val)
                prev = test
                test = test.next
        return head