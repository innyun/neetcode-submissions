# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        used = set([p.val])
        t = root
        lowest = None
        while t.val != p.val:
            used.add(t.val)
            if p.val < t.val:
                t = t.left
            else:
                t = t.right
        t = root
        while t.val != q.val:
            if t.val in used:
                lowest = t
            if q.val < t.val:
                t = t.left
            else:
                t = t.right
        if t.val in used:
            lowest = t
        return lowest