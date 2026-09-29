# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for l in lists:
            while l:
                heapq.heappush(heap, l.val)
                l = l.next
        out = None
        if heap:
            out = ListNode(heapq.heappop(heap))
        t = out
        while heap:
            t.next = ListNode(heapq.heappop(heap))
            t = t.next
        return out