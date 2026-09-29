# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
        h = head
        s = head
        f = head
        p = None
        while f and f.next:
            p = s
            s = s.next
            f = f.next.next
        if p:
            p.next = None
        p = None
        n = s.next
        while s:
            s.next = p
            p = s
            s = n
            if n:
                n = n.next
        while p and h:
            t1 = p.next
            t2 = h.next
            h.next = p
            if not t2:
                break
            h.next.next = t2
            h = t2
            p = t1

            