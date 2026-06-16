# Problem Link: https://leetcode.com/problems/odd-even-linked-list/

class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        odd = head
        even = even_head = head.next
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = even_head
        return head 