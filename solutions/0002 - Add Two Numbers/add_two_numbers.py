# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        t1, t2 = l1, l2
        head = ListNode(0)
        temp = None
        c = 0
        while(t1 != None or t2 != None or c > 0):
            d1 = 0 if t1 is None else t1.val
            d2 = 0 if t2 is None else t2.val
            d = (d1 + d2 + c) % 10
            c = (d1 + d2 + c) // 10
            if temp is None:
                head.val = d
                temp = head
            else:
                temp.next = ListNode(d)
                temp = temp.next
            t1 = t1.next if t1 is not None else t1
            t2 = t2.next if t2 is not None else t2
        return head
