# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        lookup = {}
        for i, n in enumerate(inorder):
            lookup[n] = i
        return self.helper(lookup, inorder, postorder, len(postorder), 0, len(inorder))
    
    def helper(self, lookup, inorder, postorder, post_end, in_start, in_end):
        if in_end == in_start:
            return None
        node = TreeNode(postorder[post_end - 1])
        i = lookup[postorder[post_end - 1]]
        node.left = self.helper(lookup, inorder, postorder, post_end - 1 - (in_end - i - 1), in_start, i)
        node.right = self.helper(lookup, inorder, postorder, post_end - 1, i + 1, in_end)
        return node




        
