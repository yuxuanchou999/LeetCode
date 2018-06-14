# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(root, diameter):
            if not root: return 0, diameter
            left, diameter = depth(root.left, diameter)
            right, diameter = depth(root.right, diameter)
            return 1 + max(left, right), max(diameter, 1 + left + right)
        
        return depth(root, 1)[1] - 1
        
        
        
