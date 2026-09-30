# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        d = ListNode()
        head = d

        h = []
        for l in lists: 
            while l: 
                heapq.heappush(h, l.val)
                l = l.next
        
        while h:
            d.next = ListNode(heapq.heappop(h))
            d = d.next

        return head.next