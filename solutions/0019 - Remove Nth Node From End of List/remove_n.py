# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        current = head
        nodes = []
        while current != None:
            nodes.append(current)
            current = current.next
        if n == len(nodes):
            return head.next
        nodes[-1 - n].next = nodes[0 - n].next
        return head

        
