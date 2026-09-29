# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode()
        t = out
        carry = 0
        while l1 or l2:
            s = carry
            if l1:
                s += l1.val
            if l2:
                s += l2.val
            carry = 0
            if s >= 10:
                carry = 1
                s -= 10
            t.next = ListNode(s)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            t = t.next
        if carry:
            t.next = ListNode(1)
        return out.next