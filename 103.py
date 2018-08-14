# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res, cur, level = [], [root], 1
        while cur:
            next_level, vals = [], []
            for node in cur:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            cur = next_level
            if level % 2:
                res.append(vals)
            else:
                res.append(vals[::-1])
            level += 1
        return res
                    
            
        
                
