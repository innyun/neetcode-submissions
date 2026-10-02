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
            new_node.next = tail.next
            d[tail] = new_node
            t.next = new_node
            t = t.next
            tail = tail.next
        tail = head
        t = h
        while tail:
            if tail.random == None:
                d[tail].random = None
            else:
                d[tail].random = d[tail.random]
            tail = tail.next

        return h.next