class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if k == 0 or not head or not head.next :
            return head
        
        last_node = head
        last_prev = head
        list_len = 1
        while last_node.next:
            last_prev = last_node
            last_node = last_node.next
            list_len += 1

        if k % list_len == 1:
            last_node.next = head
            head = last_node
            last_prev.next = None
            return head
        if k % list_len == 0:
            return head
        else:
            i = k % list_len
            curr = head
            while i < list_len - 1:
                curr = curr.next
                i += 1
            if last_node == curr:
                curr.next = head
                head.next = None
                return last_prev
            last_node.next = head
            head = curr.next
            curr.next = None
            return head