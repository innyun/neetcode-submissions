# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, b):
            if not b:
                return [0, False]
            if not node:
                return [0, b]
            hl, b1 = dfs(node.left, b)
            hr, b2 = dfs(node.right, b)
            if abs(hr - hl) > 1:
                return [0, False]
            return [1 + max(hl, hr), b1 and b2]
        
        return dfs(root, True)[1]
