# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s, e = head, head
        for _ in range(n+1):
            if not e:
                return head.next
            e = e.next
        while e:
            s = s.next
            e = e.next
        s.next = s.next.next
        return head
