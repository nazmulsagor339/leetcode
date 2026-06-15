# Problem Link: https://leetcode.com/problems/reverse-linked-list-ii/
class Solution(object):
    def reverseBetween(self, head, left, right):
        n = 0 
        temp = head
        left_node = None
        right_node = None
        previous_left_node = None

        # finding the left and right node
        while temp:
            n += 1
            if n == left:
                left_node = temp
            if n == right:
                right_node = temp
                break
            if not left_node:
                previous_left_node = temp
            temp = temp.next

        temp_left_node = left_node
        # reversing the node from left to right
        prev = None
        while left <= right:
            temp_next_left_node = temp_left_node.next
            temp_left_node.next = prev
            prev = temp_left_node
            temp_left_node = temp_next_left_node
            left += 1
        
        # Connecting the reversed linked list with the main linked list
        left_node.next = temp_next_left_node
        # if previous_left_node is None, that's mean we are reversing 
        #  from the head position
        if not previous_left_node:
            return prev

        previous_left_node.next = prev
        return head