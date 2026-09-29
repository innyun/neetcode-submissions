# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 1
        def dfs(m, node):
            nonlocal good
            if not node:
                return
            if node.val >= m:
                good += 1
                m = node.val
            dfs(m, node.left)
            dfs(m, node.right)
        dfs(root.val, root.left)
        dfs(root.val, root.right)
        return good
