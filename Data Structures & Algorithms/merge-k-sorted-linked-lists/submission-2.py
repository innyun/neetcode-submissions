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
        for i, l in enumerate(lists):
            if l: 
                h.append((l.val, i, l))
        heapq.heapify(h)
        
        while h:
            val, i, node = heapq.heappop(h)
            d.next = node
            d = d.next

            if node.next:
                heapq.heappush(h, (node.next.val, i, node.next))
            

        return head.next