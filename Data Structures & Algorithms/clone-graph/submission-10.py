"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        d = {}

        q = deque([node])
        new_node = None
        while q:
            for _ in range(len(q)):
                n = q.popleft()
                if n not in d:
                    new_node = Node(n.val)
                    d[n] = new_node
                else:
                    new_node = d[n]
                for adj in n.neighbors:
                    if adj not in d:
                        d[adj] = Node(adj.val)
                        q.append(adj)
                    new_node.neighbors.append(d[adj])

        return d[node]