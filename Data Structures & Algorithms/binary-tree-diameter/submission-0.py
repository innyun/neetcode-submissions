# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def recurse(node):
            nonlocal diameter
            if not node:
                return 0
            hl = recurse(node.left)
            hr = recurse(node.right)
            d = hr + hl
            diameter = max(d, diameter)
            return 1 + max(hl, hr)

        recurse(root)
        
        return diameter
