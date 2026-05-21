# Problem Link: https://leetcode.com/problems/reverse-linked-list/

#Approach: We can use three pointers to reverse the linked list. 
# We will keep track of the current node, 
# the previous node, and the next node.
class Solution(object):
    def reverseList(self, head):
        new_head = None
        current = head
        while current:
            temp = current.next
            current.next = new_head
            new_head = current
            current = temp
        return new_head