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
        if not head:
            return None
        t = head
        copy = Node(0)
        y = copy
        d = {}
        while t:
            y.next = Node(t.val)
            y = y.next
            d[t] = y
            t = t.next
        t = head
        y = copy.next
        while t:
            if not t.random:
                y.random = None
            else:
                y.random = d[t.random]
            t = t.next
            y = y.next
        return copy.next