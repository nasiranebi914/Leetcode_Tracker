# Last updated: 6/19/2025, 4:10:15 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        def sameTree(tree, subTree):
            if tree is None and subTree is None:
                return True
            if tree is None or subTree is None:
                return False
            if tree.val != subTree.val:
                return False

            return sameTree(tree.left, subTree.left) and sameTree(tree.right, subTree.right)
        
        if sameTree(root, subRoot) is True:
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)