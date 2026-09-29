# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        valid = False
        def isSameTree(root1, root2):
            if not root1 and not root2:
                return True
            if (not root1 and root2) or (not root2 and root1) or (root1.val != root2.val):
                return False
            return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)
        def traverse(root1, root2):
            nonlocal valid
            if valid:
                return
            if not root1:
                return
            if root1.val == root2.val:
                if isSameTree(root1, root2):
                    valid = True
                    return
            traverse(root1.left, root2)
            traverse(root1.right, root2)
        
        traverse(root, subRoot)
        
        return valid