# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, ma, mi):
            if not node:
                return True
            if node.val >= ma or node.val <= mi:
                return False
            return dfs(node.left, node.val, mi) and dfs(node.right, ma, node.val)
        return dfs(root, float('inf'), float('-inf'))