# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        res, stack, first, second = None, [], None, None
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break 
            node = stack.pop()
            # first time occurs reversed order
            if res and res.val > node.val:
                if not first:
                     first = res
                # first or second time occurs reversed order
                second = node
            res = node
            root = node.right
        first.val, second.val = second.val, first.val
 

