# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = []
        q = [root]
        while q:
            t = []
            level = []
            for node in q:
                if node.left:
                    t.append(node.left)
                if node.right:
                    t.append(node.right)
                level.append(node.val)
            levels.append(level)
            q = t
        return levels
