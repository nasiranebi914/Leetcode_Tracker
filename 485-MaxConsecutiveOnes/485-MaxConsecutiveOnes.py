# Last updated: 6/19/2025, 12:19:32 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0

        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.max_len = max(self.max_len, left+right)
            return max(left, right) + 1
        dfs(root)
        return self.max_len
        