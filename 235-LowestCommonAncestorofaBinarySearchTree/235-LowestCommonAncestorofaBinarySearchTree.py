# Last updated: 6/25/2025, 8:48:33 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root: return 0

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q) # if found, backtracking
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        
        return left if left else right

        