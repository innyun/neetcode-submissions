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
        while cur:
            t = None
            if cur.next:
                t = cur.next
            cur.next = p
            p = cur
            cur = t
        return p