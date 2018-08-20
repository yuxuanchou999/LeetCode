# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre: return None
        node = TreeNode(pre[0])
        if len(pre) == 1: return node
        L = post.index(pre[1]) + 1
        node.left = self.constructFromPrePost(pre[1:L + 1], post[:L])
        node.right = self.constructFromPrePost(pre[L + 1:], post[L:-1])
        return node
