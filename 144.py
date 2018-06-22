# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.pre(root, res)
        return res
    
    def pre(self, root, res):
        if not root: return
        res.append(root.val)
        self.pre(root.left, res)
        self.pre(root.right, res)
