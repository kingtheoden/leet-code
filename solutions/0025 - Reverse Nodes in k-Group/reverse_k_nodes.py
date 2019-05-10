# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k < 2:
            return head
        b = right = head
        before = end = None

        while True:
            for _ in range(k-1):
                if right:
                    right = right.next
                else:
                    return head
            if right:
                end = right.next
            else:
                return head
            top = b
            a = b
            b = b.next
            c = b.next
            for x in range(k-1):
                b.next = a
                if x < k-2:
                    a, b, c = b, c, c.next
            top.next = end
            if before:
                before.next = right
            else:
                head = right
            before = top
            b = right = end
        return head



        
