# Last updated: 6/19/2025, 10:01:19 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def get_left_depth(node):
            d = 0
            while node:
                d += 1
                node = node.left
            return d 
        
        def get_right_depth(node):
            d = 0
            while node:
                d += 1
                node = node.right
            return d
        left_depth = get_left_depth(root)
        right_depth = get_right_depth(root)

        if left_depth == right_depth:
            return (1 << left_depth) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        