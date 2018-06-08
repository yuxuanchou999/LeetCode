# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def helper(root, pre):
            if not root.left and not root.right:
                pre += '->' + str(root.val)
                res.append(pre[2:])
                return
            pre += '->' + str(root.val)
            if root.left: helper(root.left, pre)
            if root.right: helper(root.right, pre)
        
        if not root: return []
        pre, res = '', []
        helper(root, pre)
        return res
