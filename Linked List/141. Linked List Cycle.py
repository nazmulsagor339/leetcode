#Problem Link: https://leetcode.com/problems/linked-list-cycle/description/

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
#Approach 1: Using two pointers, one moves twice as fast as the other. 
# If there is a cycle, they will eventually meet. If there is no cycle, 
# the fast pointer will reach the end of the list.
        start = head
        double_start = head
        while double_start and double_start.next:
            start = start.next
            double_start = double_start.next.next
            if start == double_start:
                return True
        return False

#Approach 2: Using a set to keep track of visited nodes. 
# If we encounter a node that we've already seen, there is a cycle.
        # myset = set()
        # cur = head
        # while cur:
        #     if cur in myset:
        #         return True
        #     myset.add(cur)
        #     cur = cur.next
        # return False