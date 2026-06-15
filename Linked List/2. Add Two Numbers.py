# Problem Link: https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # creating a dummy head node for returning the sum node
        temp = dummy_head = ListNode()
        sum1 = 0 # store the sum of l1
        sum2 = 0 # store the sum of l2
        power = 0 # power of 10^0, 10^1 ans so on
        while l1:
            # technique to calculate the sum
            # (2 * 10^0) + (4 * 10^1) + (3 * 10^2)
            sum1 = sum1 + (l1.val * (10 ** power))
            power += 1
            l1 = l1.next
        power = 0
        while l2:
            sum2 = sum2 + (l2.val * (10 ** power))
            power += 1
            l2 = l2.next

        total_sum = sum1 + sum2
        if total_sum == 0:
            return dummy_head
        while total_sum != 0:
            rem = total_sum % 10
            new_node = ListNode(val=rem)
            temp.next = new_node
            temp = temp.next
            total_sum = total_sum // 10
        return dummy_head.next