# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def helper(root, prev, sum):
            if not root: return 0
            cur = prev + root.val
            return int(cur == sum) + helper(root.left, cur, sum) + helper(root.right, cur, sum)
        
        if not root: return 0
        return helper(root, 0, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
