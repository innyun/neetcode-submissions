# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        p = None
        cur = head
        n = head.next
        while cur:
            t = None
            if n:
                t = n.next
            cur.next = p
            p = cur
            cur = n
            n = t
        return p