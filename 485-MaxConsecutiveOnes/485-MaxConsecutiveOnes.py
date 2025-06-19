# Last updated: 6/19/2025, 2:40:56 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if left == -1 or right == -1 or abs(right - left) > 1:
                return -1
            return max(left,right)+1
        result = dfs(root)
        if result is -1:
            return False
        return True

        