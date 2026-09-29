# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid = True
        def dfs(node, ma, mi):
            nonlocal valid
            if not valid:
                return
            if node.val >= ma or node.val <= mi:
                valid = False
                return
            if node.left:
                if node.left.val >= node.val:
                    valid = False
                    return
                dfs(node.left, node.val, mi)
            if node.right:
                if node.right.val <= node.val:
                    valid = False
                    return
                dfs(node.right, ma, node.val)
        dfs(root, 1001, -1001)
        return valid