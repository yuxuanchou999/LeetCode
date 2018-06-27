# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """    
        return self.dfs(root)[1]
    
    def dfs(self, root):
        if not root: return (0, 0)
        l, r = self.dfs(root.left), self.dfs(root.right)
        return (l[1] + r[1], max(l[1] + r[1], l[0] + r[0] + root.val))
        
