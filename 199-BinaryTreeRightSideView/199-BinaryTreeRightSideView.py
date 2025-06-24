# Last updated: 6/23/2025, 9:47:10 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:        
        def dfs(node, max_so_far):
            if node is None:
                return 0
            if node.val >= max_so_far:
                counter = 1
            else:
                counter = 0
            max_so_far = max(max_so_far, node.val)
            counter += dfs(node.left, max_so_far)
            counter += dfs(node.right, max_so_far)
            return counter
                
        return dfs(root, root.val)
