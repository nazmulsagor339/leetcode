# Problem Link: https://leetcode.com/problems/copy-list-with-random-pointer/

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        temp = {}
        curr = head
        #creating the copy node
        while curr:
            new_node = Node(curr.val)
            temp[curr] = new_node
            curr = curr.next
        curr = head
        #connecting the new copy node
        while curr:
            copy = temp[curr]
            copy.next = temp[curr.next] if curr.next else None
            copy.random = temp[curr.random] if curr.random else None
            curr = curr.next
        return temp[head]