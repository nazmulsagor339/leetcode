class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_A = 1
        len_B = 1
        currA = headA
        currB = headB
        while currA.next or currB.next:
            if currA == currB:
                break
            if currA.next:
                len_A += 1
                currA = currA.next
            if currB.next:
                len_B += 1
                currB = currB.next
        if currA != currB:
            return None
        currA = headA
        currB = headB
        if len_A > len_B:
            while len_A - len_B:
                currA = currA.next
                len_B += 1
        else:
            while len_B - len_A:
                currB = currB.next
                len_A += 1
        while currA != currB:
            currA = currA.next
            currB = currB.next
        return currA