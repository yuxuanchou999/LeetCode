# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(root, less, large):
            if not root: return True
            if root.val >= less or root.val <= large: return False
            return helper(root.left, min(less, root.val), large) and helper(root.right, less, max(root.val, large))
                  
        return helper(root, float('inf'), float('-inf'))
