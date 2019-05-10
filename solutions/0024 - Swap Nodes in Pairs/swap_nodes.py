# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        current = head
        last = None
        while current and current.next:
            one, two, three = current, current.next, current.next.next
            one.next, two.next = three, one
            if last:
                last.next = two
            else:
                head = two
            last = one
            current = three
        return head

        
