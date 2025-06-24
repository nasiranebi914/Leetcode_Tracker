# Last updated: 6/23/2025, 9:49:13 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_seen) -> int:
            if node is None:
                return 0
            
            i = 0
            if node.val >= max_seen:
                max_seen = node.val
                i = 1

            return i + dfs(node.left, max_seen) + dfs(node.right, max_seen)

        return dfs(root, float('-inf'))


    # def goodNodes(self, root: TreeNode) -> int:
    #     stack = [(root, float('-inf'))]
    #     ans = 0
    #     while stack:
    #         node, max_seen = stack.pop()
    #         if node:
    #             if max_seen <= node.val:
    #                 max_seen = node.val
    #                 ans += 1

    #             stack.append((node.left, max_seen))
    #             stack.append((node.right, max_seen))

    #     return ans