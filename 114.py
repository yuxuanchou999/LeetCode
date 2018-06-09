# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.helper(root, None)
    
    def helper(self, root, head):
        if root:
            head = self.helper(root.right, head)
            head = self.helper(root.left, head)
            root.right = head
            root.left = None
            return root
        else:
            return head
        
        
