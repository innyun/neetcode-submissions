"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {}
        h = Node(1)
        t = h
        tail = head
        while tail:
            new_node = Node(tail.val)
            d[tail] = new_node
            t.next = new_node
            t = t.next
            tail = tail.next
        for k in d:
            if k.random == None:
                d[k].random = None
            else:
                d[k].random = d[k.random]
            k = k.next

        return h.next