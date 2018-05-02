# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        Iterative:
				if not root: return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            p, q = stack.pop(), stack.pop()
            if not p and not q:
                continue
            if not p or not q or p.val != q.val:
                return False
            stack.append(p.left)
            stack.append(q.right)
            stack.append(p.right)
            stack.append(q.left)
            
        return True

        Recursive:
	if not root:
            return True
        return self.func(root.left, root.right) 
    
        def func(self, left, right):
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            return self.func(left.left, right.right) and self.func(left.right, right.left)
            
