# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = [x for x in lists if x]
        if not lists:
            return None
        lists.sort(key=lambda x: x.val)
        result = ListNode(lists[0].val)
        current = result
        if lists[0].next is None:
            del lists[0]
        else:
            lists[0] = lists[0].next
            lists.sort(key=lambda x: x.val)
        while lists:
            current.next = ListNode(lists[0].val)
            current = current.next
            if lists[0].next is None:
                del lists[0]
            else:
                lists[0] = lists[0].next
                lists.sort(key=lambda x: x.val)

        return result
        
