# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        last = []
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                n = q.pop()
                if n.left:
                    q.appendleft(n.left)
                if n.right:
                    q.appendleft(n.right)
                level.append(n.val)
            last.append(level[-1])
        return last