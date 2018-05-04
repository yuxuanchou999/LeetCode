# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    maxsum = -float('inf')
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.pathsum(root)
        return self.maxsum
    
    def pathsum(self, root):
        if not root:
            return 0
        left = max(0, self.pathsum(root.left))
        right = max(0, self.pathsum(root.right))
        self.maxsum = max(self.maxsum, root.val + left + right)
        return root.val + max(left, right)
       

    
    
