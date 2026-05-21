# Problem link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        prevNode = head
        currentNode = head
        if head:
            nextNode = currentNode.next
        else:
            nextNode = head
        while nextNode:
            if currentNode.val == nextNode.val:
                while currentNode.val == nextNode.val:
                    currentNode.next = nextNode.next
                    nextNode = nextNode.next
                    if not nextNode:
                        break
                if head == currentNode:
                    currentNode = nextNode
                    head = currentNode
                else:
                    currentNode = nextNode
                if nextNode:
                    nextNode = currentNode.next
                prevNode.next = currentNode 

            else:
                prevNode = currentNode
                currentNode = nextNode
                nextNode = nextNode.next
        return head