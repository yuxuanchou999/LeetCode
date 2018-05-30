# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        stack = [root]
        res = [[root.val]]
        while stack:
            new, v = [], []
            while stack:
                node = stack.pop(0)
                if node.left: 
                    new.append(node.left)
                    v.append(node.left.val)
                if node.right: 
                    new.append(node.right)
                    v.append(node.right.val)
            if v: res.append(v)
            stack = new
        return res
            
        
