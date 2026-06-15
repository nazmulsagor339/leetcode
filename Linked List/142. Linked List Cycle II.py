# Problem Link: https://leetcode.com/problems/linked-list-cycle-ii/

class Solution(object):
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # if the condition is true, means there is a cycle
            if slow == fast:
                # moving slow to the head again, because if we
                # move slow from the head and fast node to the next node at a time
                # it will meet at the begining of the cycle. And that's how we can
                # find the starting point of the cycle
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None