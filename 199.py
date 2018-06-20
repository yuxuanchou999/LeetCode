# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        cur, new, res = [root], [], []
        while cur:
            x = cur.pop(0)
            if x.left: new.append(x.left)
            if x.right: new.append(x.right)
            if not cur: 
                res.append(x.val)
                cur += new
                new = []
                
        return res
            
            
