# Problem Link: https://leetcode.com/problems/reorder-list/
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head.next or not head.next.next:
            return head
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        prev = None
        reverse_head = slow.next
        slow.next = None
        # reversing the list
        while reverse_head:
            temp = reverse_head.next
            reverse_head.next = prev
            prev = reverse_head
            reverse_head = temp
        temp1 = head
        curr = head.next
        temp2 = prev
        while temp1 and temp2:
            temp1_next, temp2_next = temp1.next, temp2.next
            temp1.next = temp2
            temp2.next = temp1_next
            temp1, temp2 = temp1_next, temp2_next