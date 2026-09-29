# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(m, node):
            if not node:
                return 0
            res = 0
            if node.val >= m:
                res = 1
                m = node.val
            res += dfs(m, node.left)
            res += dfs(m, node.right)
            return res
        return dfs(root.val, root)
