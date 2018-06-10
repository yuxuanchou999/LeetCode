# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        res = []
        self.helper(root, 0, res)
        return sum in res
    
    def helper(self, root, v, res):
        if not root: return
        v += root.val
        if not root.left and not root.right: res.append(v)
        self.helper(root.left, v, res)
        self.helper(root.right, v, res)
        
